# -*- coding:utf-8 -*-

from nameko.dependency_providers import Config
from nameko.rpc import rpc
from mongo_util import MongoIns
from bson import ObjectId

class SmlibToolService:
    name = "smlibToolService"

    # 配置文件
    config = Config()

    @property
    def host(self):
        return self.config['MONGO_CONFIG']['sensorcmd']['DB_HOST']
    @property
    def dbname(self):
        return self.config['MONGO_CONFIG']['sensorcmd']['DB_NAME']
    
    @rpc
    def get_monitors(self, code_name=None, data_type=None, packet_name=None, sensor_type=None):
        """
            1. 根据项目代号(code_name), 数据类型(data_type), 数据来源(packet_name), 传感类型(sensor_type), 获取所有的传感数据
            2. 如果传递sensor_type, 则返回单个传感数据(字典); 否则返回数组
        """
        # 获取所有的传感类型
        monitors, _ = MongoIns().m_list('monitor', host=self.host, dbname=self.dbname, findall=True)
        # 如果传递项目代码, 则读取项目级别的传感类型
        if code_name:
            m, _ = MongoIns().m_list('monitor', host=self.host, dbname=code_name, findall=True)
            # 如果项目级别的传感类型和通用的传感类型冲突(code_name: 这里的code_name指的是传感类型, 而非项目代号), 则以项目级别为准
            monitors = filter(lambda item: item.get('code_name') not in [i.get('code_name') for i in m], monitors)
            monitors.extend(m)
        
        # 传递data_type(数据类型, '0'为传感器数据, '1'为状态数据. 如果为空, 则默认为'0')
        if data_type:
            monitors = [item for item in monitors if item.get('data_type') == data_type]
        # 传递packet_name(数据来源, src_data为数组)
        if packet_name:
            monitors = [item for item in monitors if packet_name in (item.get('src_data') or [])]
        # 传递sensor_type(传感类型)
        if sensor_type:
            monitors = [item for item in monitors if item.get('code_name') == sensor_type]
            return monitors[0] if monitors else {}
        
        return monitors

    @rpc
    def get_data_params(self, code_name=None, sensor_type=None):
        """根据项目代号(code_name), 传感类型(sensor_type), 获取数据输入参数"""
        monitor = self.get_monitors(code_name=code_name, sensor_type=sensor_type)
        return monitor.get('params', [])

    @rpc
    def get_calc_params(self, code_name=None, sensor_type=None):
        """根据项目代号(code_name), 传感类型(sensor_type), 获取数据计算参数"""
        calc_params = self.get_monitors(code_name=code_name, sensor_type=sensor_type).get('calc_params', []) or []
        d = MongoIns().m_find_one('calc_formula_params', host=self.host, dbname=code_name).get('calc_params', []) or []
        calc_params.extend(d)
        return calc_params

    @rpc
    def get_formula_params(self, code_name=None, sensor_type=None):
        """根据项目代号(code_name), 传感类型(sensor_type), 获取数据计算输出"""
        formula_params = self.get_monitors(code_name=code_name, sensor_type=sensor_type).get('formula_params', []) or []
        d = MongoIns().m_find_one('calc_formula_params', host=self.host, dbname=code_name).get('formula_params', []) or []
        formula_params.extend(d)
        return formula_params

    @rpc
    def get_main_monitor(self, code_name=None, sensor_type=None):
        """根据项目代号(code_name), 传感类型(sensor_type), 获取主监测项"""
        params = self.get_data_params(code_name=code_name, sensor_type=sensor_type) + self.get_formula_params(code_name=code_name, sensor_type=sensor_type)
        mapCodeParams = dict((p.get('code'), p) for p in params)
        main_monitor_item = MongoIns().m_find_one('calc_formula_params', host=self.host, dbname=code_name, code_name=sensor_type).get('main_monitor_item')
        return mapCodeParams.get(main_monitor_item, {}) or {}

    @rpc
    def restore_series_data(data):
        """还原时间序列数据(备注: 没看懂)"""
        # 数据特定key
        COLUMN_FIXED = ['_id', 'code_name', 'gateway_id', 'sensor_type', 'node_id', 'channel', 'dtime', 'statistic']

        ts = data.get('ts')
        data_key = 'ts'

        split_data = []
        for no, _ts in enumerate(ts):
            d = {}
            for k, v in data.items():
                if k in COLUMN_FIXED: d[k] = v 
                elif k.endswith('_ts'):
                    continue
                elif len(v) == len(ts):
                    d[k] = v[no]
                else:
                    k_ts = data.get(k + '_ts')
                    if not k_ts:
                        if len(v) < len(ts): v = [v[0]] * len(ts)
                        d[k] = v[no]
                    else:
                        k_ts = k_ts[0: no + 1]
                        i0 = sum([item[1] for item in k_ts[0:no]])
                        i1 = sum([item[1] for item in k_ts])
                        d[k] = v[i0: i1] 

            split_data.append(d)

        return split_data
        