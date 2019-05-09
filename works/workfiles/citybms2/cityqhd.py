# -*- coding:utf-8 -*-

import os, time
from bson import ObjectId
from multiprocessing import Pool
from mongo_util import MongoIns
m_util = MongoIns()

from pymongo import MongoClient

host = '192.168.111.5:27011'
dbname = 'sjz'

cityqhd = 'cityqhd'
cityqhd_host = '121.22.33.134:27017'

cas = 'cas'
cas_host = '192.168.111.149:27017'

# 结构类型、养护单位、管理单位、巡检人员
def mapInfo():
    bridgepart, _ = m_util.m_list('bridgepart', host=host, dbname=dbname, findall=True)
    mapPart = dict((item['_id'], item.get('name', '')) for item in bridgepart)
    data = {
        'options': mapPart,
        'code':'bridgetype',
        'label':'结构类型'
    }
    m_util.m_update('options', {'code': 'bridgetype'}, dbname=cityqhd, host=cityqhd_host, upsert=True, **data)

    company, _ = m_util.m_list('company', host=host, dbname=dbname, findall=True)
    mapCompany = dict((item['_id'], item.get('name', '')) for item in company)

    data = {
        'options': mapCompany,
        'code': 'yanghdw',
        'label': '养护单位',
        'type': '1'
    }
    m_util.m_update('options', {'code': 'yanghdw'}, dbname=cityqhd, host=cityqhd_host, upsert=True, **data)
    data = {
        'options': mapCompany,
        'code': 'guanldw',
        'label': '管理单位',
        'type': '0'
    }
    m_util.m_update('options', {'code': 'guanldw'}, dbname=cityqhd, host=cityqhd_host, upsert=True, **data)

    passport, _ = m_util.m_list('passport', host=cas_host, dbname=cas, findall=True, attribute='customer')
    mapPassport = dict((item['_id'], [item.get('nickname', ''), item.get('username', '')]) for item in passport)
    data = {
        'options': mapPassport,
        'code': 'xunjry',
        'label': '巡检人员'
    }
    m_util.m_update('options', {'code': 'xunjry'}, dbname=cityqhd, host=cityqhd_host, upsert=True, **data)

# mapInfo()

# 桥梁信息表
def upsert_bridge():
    bridges, _ = m_util.m_list('bridgeinfo', host=host, dbname=dbname, findall=True)
    for b in bridges:
        m_util.m_update('bridgeinfo', {'_id': ObjectId(b.pop('_id'))},
                        host=cityqhd_host, dbname=cityqhd, upsert=True, **b)

# upsert_bridge()

# 道路信息表、路段信息表
def upsert_road():
    roads, _ = m_util.m_list('roadinfo', host=host, dbname=dbname, findall=True)
    for r in roads:
        m_util.m_update('roadinfo', {'_id': ObjectId(r.pop('_id'))},
                        host=cityqhd_host, dbname=cityqhd, upsert=True, **r)

    roadsections, _ = m_util.m_list('roadsection', host=host, dbname=dbname, findall=True)
    for rs in roadsections:
        m_util.m_update('roadsection', {'_id': ObjectId(rs.pop('_id'))},
                        host=cityqhd_host, dbname=cityqhd, upsert=True, **rs)

# upsert_road()

# 桥梁巡检表
def upsert_xunjian():
    client_host, client_port = cityqhd_host.split(':')
    client = MongoClient(host=client_host, port=int(client_port))
    tb = client[cityqhd]['bridgexunjian']

    data = tb.find({}).sort([('_id', -1)]).limit(1)
    data = list(data)
    if data:
        _id = data[0].get('_id', 0.0)
    else:
        data = m_util.m_find_one('bridgexunjian', host=host, dbname=dbname)
        _id = data.get('_id')

    while True:
        bridge_xunjian, _ = m_util.m_list('bridgexunjian', host=host, dbname=dbname, findall=True,
                                          page_size=1000, _id={'$gte': ObjectId(_id)}, sorts=[('_id', 1)])

        last_id = 0
        for bx in bridge_xunjian:
            if bx.get('_id') > last_id:
                last_id = bx['_id']
            m_util.m_update('bridgexunjian', {'_id': ObjectId(bx.pop('_id'))},
                            host=cityqhd_host, dbname=cityqhd, upsert=True, **bx)

        print('update to', last_id, len(bridge_xunjian))
        if len(bridge_xunjian) < 1000:
            break
        else:
            _id = last_id
upsert_xunjian()

# 道路巡检表
def upsert_roadxunjian():
    client_host, client_port = cityqhd_host.split(':')
    client = MongoClient(host=client_host, port=int(client_port))
    tb = client[cityqhd]['road_xunj_disease']

    data = tb.find({}).sort([('_id', -1)]).limit(1)
    data = list(data)
    if data:
        _id = data[0].get('_id', 0.0)
    else:
        data = m_util.m_find_one('road_xunj_disease', host=host, dbname=dbname)
        _id = data.get('_id')

    while True:
        road_xunjian, _ = m_util.m_list('road_xunj_disease', host=host, dbname=dbname, findall=True,
                                        page_size=1000, _id={'$gte': ObjectId(_id)}, sorts=[('_id', 1)])
        last_id = _id
        for rx in road_xunjian:
            if rx.get('_id') > last_id:
                last_id = rx['_id']
            m_util.m_update('road_xunj_disease', {'_id': ObjectId(rx.pop('_id'))},
                            host=cityqhd_host, dbname=cityqhd, upsert=True, **rx)

        if len(road_xunjian) < 1000:
            break
        else:
            _id = last_id

# upsert_roadxunjian()

# 桥梁维修记录表
def upsert_weixiu():
    client_host, client_port = cityqhd_host.split(':')
    client = MongoClient(host=client_host, port=int(client_port))
    tb = client[cityqhd]['bridge_repair']

    data = tb.find({}).sort([('addon', -1)]).limit(1)
    data = list(data)
    if data:
        addon = data[0].get('addon', '')
    else:
        data = m_util.m_find_one('bridge_repair', host=host, dbname=dbname)
        addon = data.get('addon')

    while True:
        weixiu, _ = m_util.m_list('bridge_repair', host=host, dbname=dbname, findall=True, page_size=1000,
                                  addon={'$gte': addon}, sorts=[('addon', 1)])
        last_addon = ''
        for w in weixiu:
            if w.get('addon') > last_addon:
                last_addon = w['addon']
            m_util.m_update('bridge_repair', {'_id': ObjectId(w.pop('_id'))},
                        host=cityqhd_host, dbname=cityqhd, upsert=True, **w)

        if len(weixiu) < 1000:
            break
        else:
            addon = last_addon
upsert_weixiu()

# 道路维修记录表
def upsert_roadweixiu():
    client_host, client_port = cityqhd_host.split(':')
    client = MongoClient(host=client_host, port=int(client_port))
    tb = client[cityqhd]['road_xunj_repair']

    data = tb.find({}).sort([('addon', -1)]).limit(1)
    data = list(data)
    if data:
        addon = data[0].get('addon', '')
    else:
        data = m_util.m_find_one('road_xunj_repair', host=host, dbname=dbname)
        addon = data.get('addon')

    while True:
        weixiu, _ = m_util.m_list('road_xunj_repair', host=host, dbname=dbname, findall=True, page_size=1000,
                                  addon={'$gte': addon}, sorts=[('addon', 1)])
        last_addon = ''
        for w in weixiu:
            if w.get('addon') > last_addon:
                last_addon = w['addon']
            m_util.m_update('road_xunj_repair', {'_id': ObjectId(w.pop('_id'))},
                            host=cityqhd_host, dbname=cityqhd, upsert=True, **w)

        if len(weixiu) < 1000:
            break
        else:
            addon = last_addon
# upsert_roadweixiu()


# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     mapInfo()
#     upsert_bridge()
#     upsert_road()
#     p = Pool(20)
#     start = time.time()
#     for i in range(20):
#         p.apply_async(upsert_xunjian)
#         p.apply_async(upsert_roadxunjian)
#         p.apply_async(upsert_weixiu)
#         p.apply_async(upsert_roadweixiu)
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     end = time.time()
#     print 'end - start: ', end - start
#     print('All subprocesses done.')



