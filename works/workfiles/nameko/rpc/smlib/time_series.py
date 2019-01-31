# -*- coding:utf-8 -*-

import json
import math
import time
import numpy as np

from datetime import datetime
from tornado import gen
from bson import ObjectId, SON
from kpages import get_context

from nameko.dependency_providers import Config
from nameko.rpc import rpc, RpcProxy
from mongo_util import MongoIns

# 时间格式
FORMAT_TS_S = "%Y-%m-%d_%H-%M-%S"
FORMAT_TS_M = "%Y-%m-%d_%H-%M"
FORMAT_TS_H = "%Y-%m-%d_%H"
FORMAT_TS_D = "%Y-%m-%d"

class SmlibTimeSeriesService:
    name = "smlibTimeSeriesService"

    config = Config()

    toolService = RpcProxy('smlibToolService')

    @property
    def host(self):
        return self.config['MONGO_CONFIG']['sensorcmd']['DB_HOST']
    @property
    def dbname(self):
        return self.config['MONGO_CONFIG']['sensorcmd']['DB_NAME']

    @rpc
    def get_id(self, node_id, channel, ts, f = FORMAT_TS_M):
        if channel not in [None, '']:
            _id   = "{}_{}_{}".format(node_id,channel,time.strftime(f,time.localtime(ts)))
        else:
            _id = "{}_{}".format(node_id,time.strftime(f,time.localtime(ts)))

        return _id

    @rpc
    def series(self, code_name, sensor_type, sensor_id, start, end, output='val', modal='l', isfilter=0, **kwargs):
        """
            参数解释:
                code_name: 项目代号
                sensor_type: 传感类型
                sensor_id: 测点号
                start: 起始时间
                end: 终止时间
                output: 绘制项目
                modal: l(line), k(k线)
                zoom: d(天), h(小时), m(分钟), src(原始); 如果不是d, h, m, src, 则按照: 3天以上为d, 1~3天为h, 否则为m的规则进行
        """
        # 判断zoom的正确格式
        zoom = kwargs.get('zoom')
        if zoom not in ['d', 'h', 'm', 'src']:
            if end - start >= 60 * 60 * 24 * 3:
                zoom = 'd'
            elif end - start >= 60 * 60 * 24 * 1 - 1:
                zoom = 'h'
            else:
                zoom = 'm'
        # 数据表的格式为: data_ + 传感类型 + _ + zoom
        table = 'data_{}{}'.format(sensor_type, '_'+zoom if zoom in ['d', 'h'] else "")
        _format = eval('FORMAT_TS_{}'.format(zoom.upper() if zoom in ['d', 'h', 'm'] else 'M'))

        # 获取测点信息
        sensor = MongoIns().m_find_one('sensors', host=self.host, dbname=code_name, sensor_id=sensor_id, sensor_type=sensor_type)
        if not sensor or not sensor.get('node_id', None): return {}

        # 数据表的_id由node_id + channel(可能为空) + ts组成
        _id_start = self.get_id(sensor['node_id'], sensor.get('channel'), start, f = _format)
        _id_end = self.get_id(sensor['node_id'], sensor.get('channel'), end, f = _format)
        cond = {'$or': [{'_id': {'$gte': _id_start, '$lte': _id_end}}]}
        # 存在历史节点, 需要增加过滤
        for old_node in sensor.get('old_nodes') or []:
            o_id_start = self.get_id(old_node['node_id'], old_node.get('channel'), start, f = _format)
            o_id_end = self.get_id(old_node['node_id'], old_node.get('channel'), end, f = _format)
            cond['$or'].append({'_id': {'$gte': o_id_start, '$lte': o_id_end}})

        # 支持多个绘制项目的传入, 但实际调用中通常为单个绘制项目
        output = output.split(',')
        # 获取输入参数
        data_params = self.toolService.get_data_params(code_name, sensor_type)
        # 获取计算输出
        formula_params = self.toolService.get_formula_params(code_name, sensor_type)

        # 这里path是历史保留字段, 通常path=code, 但是存在如下特殊的问题(以下注释摘自: sensorcmd-web/monitor.md文本)
        # 假设传感网传递的数据为:{code: temp, str: {temp: 12}}, 则我们通过str.temp来获取数据.
        # 但目前传感网传递的数据格式为: {code: temp, temp: 12}, 所以path == code.
        data_params = dict((item.get('code'), item.get('path')) for item in data_params)
        data_params.update(dict((item.get('code'), item.get('code')) for item in formula_params))

        output_reverse_map = {}
        for no, op in enumerate(output):
            output[no] = data_params.get(op) or op
            output_reverse_map[output[no]] = op

        # 获取主监测项
        main_monitor_item = MongoIns().m_find_one('calc_formula_params', host=self.host, dbname=code_name, code_name=sensor_type).get('main_monitor_item')

        fields = dict(('statistic.{}'.format(op), 1) for op in output)
        fields.update({'_id': 1,'dtime': 1, 'ts': 1})
        cond.update(dict(('statistic.{}.n'.format(op), {'$exists':1}) for op in output))

        data = dict((op, {'x':[], 'y': [], 'std': [], 'maxs': [], 'mins': [], 'tips': ''}) for op in output)
        # 如果是line并且获取原始值
        if modal == 'l' and zoom == 'src':
            # 获取前10条数据, 通过statistic.*.n的数据, 让40000/n, 保证数据量最多只有4万条.
            # 这里n可能代表一次传递的数据条数(不太确定..)
            result, _ = MongoIns().m_list(table, host=self.host, dbname=code_name, fields=fields, page_size=10, **cond)

            count_map = dict((op, 0) for op in output)
            for r in result:
                for op in output:
                    count_map[op] = count_map[op] + r['statistic'][op]['n']

            count = max(count_map.values())
            if not count: return {}
            # 最多限制4万条数据
            COUNT_LIMIT = 40000
            limit = int(COUNT_LIMIT/(count / 10.0))

            # 主监测项的数据
            if data_params.get(main_monitor_item) in output:
                _id_s = self.get_id(sensor['node_id'], sensor.get('channel'), start - 3600 * 0, f=FORMAT_TS_D)
                _id_e = self.get_id(sensor['node_id'], sensor.get('channel'), end, f=FORMAT_TS_D)
                cond_d = {'_id': {'$gte': _id_s, '$lte': _id_e}}

                # 均值和方差由天的数据获取, 并且取的是平均值
                result_d, _ = MongoIns().m_list('data_{}_d'.format(sensor_type), host=self.host, dbname=code_name, fields=fields, findall=True, **cond_d)

                mean = [r.get('statistic', {}).get(data_params.get(main_monitor_item), {}).get('mean',0) for r in result_d]
                mean = [i for i in mean if not np.isnan(i)]
                mean = sum(mean)/(len(mean) or 1)
                std = [r.get('statistic', {}).get(data_params.get(main_monitor_item), {}).get('std',0) for r in result_d]
                std = [i for i in std if not np.isnan(i)]
                std = sum(std)/(len(std) or 1)

            _id_start = self.get_id(sensor['node_id'], sensor.get('channel'), start, f=FORMAT_TS_M)
            _id_end = self.get_id(sensor['node_id'], sensor.get('channel'), end, f=FORMAT_TS_M)

            fields = {'_id': 1,'dtime': 1,'sample_interval':1,'ts':1}
            [fields.update({op: 1, '{}_ts'.format(op): 1}) for op in output]

            # 查询4万条数据(或4万条以下), 并且按照时间排序
            cursor, _ = MongoIns().m_list(table, host=self.host, dbname=code_name, fields=fields, page_size=limit, sorts=[('_id',-1)], **cond)
            cursor = sorted(cursor, key=lambda x:x.get('dtime'))
            # 被过滤的数量
            filter_count = 0
            for doc in cursor:
                for op in output:
                    val = doc.get(op)
                    ts = doc.get('{}_ts'.format(op)) or doc.get('ts')
                    val = [float(v) for v in val]
                    # 时间和值要一一对应
                    if len(val) != len(ts):
                        try:
                            sample_interval = doc.get('sample_interval',[0])[0]
                            ts = [(item[0] + i * sample_interval) for item in ts  for i in range(item[1])]
                        except Exception as e:
                            pass

                    _ts = []
                    _val = []
                    # 过滤规则: 大于 均值 - 3 * 方差, 小于 均值 + 3 * 方差
                    if data_params.get(main_monitor_item) == op and isfilter:
                        for i, v in enumerate(val):
                            if v >= mean - 3*std and v <= mean + 3*std:
                                _ts.append(ts[i])
                                _val.append(v)
                            else:
                                filter_count += 1

                        ts = _ts
                        val = _val
                    data[op]['x'].extend(sorted(ts))
                    data[op]['y'].extend(val)

            # 根据绘制项目, 整理实际的数据
            for op in output:
                # 最多展示4万条数据(因为数据库中的每条数据, ts和val的长度不一定为1, 所以导致x/y的数据实际上会超过4万条, 这里做一层过滤)
                data[op]['x'] = data[op]['x'][-1 * COUNT_LIMIT:]
                data[op]['y'] = data[op]['y'][-1 * COUNT_LIMIT:]
                zip_xy = zip(data[op]['x'], data[op]['y'])
                zip_xy = sorted(zip_xy, key = lambda _x: _x[0])
                data[op]['x'] = [_x[0] for _x in zip_xy]
                data[op]['y'] = [_x[1] for _x in zip_xy]

                data[op]['std'] = [0] * len(data[op]['x'])
                data[op]['maxs'] = data[op]['y']
                data[op]['mins'] = data[op]['y']

                data[op]['tips'] = u' ({})'.format(len(data[op]['x']))
                if filter_count:
                    data[op]['tips'] = data[op]['tips'] +u', filtered {}'.format(filter_count)

                data[op]['y'] = [float(x) if x not in ['null', ''] else 0 for x in data[op]['y']]
                if data[op]['y']:
                    data[op]['mean'] = np.mean(data[op]['y'])
                    data[op]['max'] = np.max(data[op]['y'])
                    data[op]['min'] = np.min(data[op]['y'])
        elif modal == 'l':
            # 由于不是原始值, 所以数量上无需进行限制
            result, _ = MongoIns().m_list(table, host=self.host, dbname=code_name, fields=fields, findall=True, **cond)
            result = sorted(result, key=lambda x:x.get('dtime'))
            for r in result:
                dtime = str(r.get('dtime'))
                ts = time.mktime(time.strptime(dtime, "%Y-%m-%d %H:%M:%S"))
                for op in output:
                    statistic = r['statistic'][op]
                    if not statistic.get('mean'): continue
                    if np.isnan(statistic.get('mean')): continue

                    data[op]['x'].append(ts)
                    data[op]['y'].append(statistic.get('mean'))
                    data[op]['std'].append(0 if np.isnan(statistic.get('std')) else statistic.get('std'))
                    data[op]['maxs'].append(statistic.get('max'))
                    data[op]['mins'].append(statistic.get('min'))

            for op in output:
                if data[op]['y']:
                    data[op]['mean'] = np.mean(data[op]['y'])
                    data[op]['max'] = np.max(data[op]['y'])
                    data[op]['min'] = np.min(data[op]['y'])
        elif modal == 'k':
            # 这里k线的逻辑, 并不太清楚
            result, _ = MongoIns().m_list(table, host=self.host, dbname=code_name, fields=fields, findall=True, **cond)

            data = dict((op, []) for op in output)
            data = dict((op, {'ts':[], 'max': [], 'min': [], 'mean':[], 'mean2':[], 'std': [], 'n': []}) for op in output)
            for r in result:
                dtime = str(r.get('dtime'))
                ts = time.mktime(time.strptime(dtime, "%Y-%m-%d %H:%M:%S"))
                for op in output:
                    statistic = r['statistic'][op]

                    if statistic.get('mean') == None: continue
                    if statistic.get('std') == None: continue

                    if np.isnan(statistic.get('mean')): continue
                    if np.isnan(statistic.get('std')): continue

                    data[op]['ts'].append(ts)
                    data[op]['n'].append(statistic.get('n'))
                    data[op]['mean'].append(statistic.get('mean'))
                    data[op]['mean2'].append(statistic.get('mean2'))
                    data[op]['std'].append(statistic.get('std'))
                    data[op]['max'].append(statistic.get('max'))
                    data[op]['min'].append(statistic.get('min'))

                    data[op]['max'][-1] = max(data[op]['max'][-1], data[op]['mean'][-1]+data[op]['std'][-1])
                    data[op]['min'][-1] = min(data[op]['min'][-1], data[op]['mean'][-1]-data[op]['std'][-1])

        for k, v in data.items():
            if k.endswith('_yd'): continue
            i = data.pop(k)
            data[output_reverse_map.get(k)] = i

        data = dict(zoom=zoom, data = data, modal=modal)
        return data
