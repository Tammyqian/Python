# -*- coding:utf-8 -*-

from bson import ObjectId
from mongo_util import MongoIns
m_util = MongoIns()
host = '192.168.111.5:27011'
dbname = 'sjz'

cityqhd = 'cityqhd'
cityqhd_host = '192.168.111.5:27011'

def mapInfo():
    bridgepart, _ = m_util.m_list('bridgepart', host=host, dbname=dbname, findall=True)
    mapPart = dict((item['_id'], item.get('name', '')) for item in bridgepart)
    data = {
        'options': mapPart,
        'code':'bridgetype',
        'label':'结构类型',
    }
    m_util.m_update('options', {'code': 'bridgetype'}, dbname=cityqhd, host=cityqhd_host, upsert=True, **data)

# mapInfo()

def upsert_bridge():
    bridges, _ = m_util.m_list('bridgeinfo', host=host, dbname=dbname, findall=True)
    for b in bridges:
        m_util.m_update('bridgeinfo', {'_id': ObjectId(b.pop('_id'))},
                        host=cityqhd_host, dbname=cityqhd, upsert=True, **b)

# upsert_bridge()

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


def upsert_xunjian():
    bridge_xunjian, _ = m_util.m_list('bridgexunjian', host=host, dbname=dbname, findall=True)
    for bx in bridge_xunjian:
        m_util.m_update('bridgexunjian', {'_id': ObjectId(bx.pop('_id'))},
                        host=cityqhd_host, dbname=cityqhd, upsert=True, **bx)

# upsert_xunjian()

def upsert_roadxunjian():
    road_xunjian, _ = m_util.m_list('road_xunj_disease', host=host, dbname=dbname, findall=True)
    for rx in road_xunjian:
        m_util.m_update('road_xunj_disease', {'_id': ObjectId(rx.pop('_id'))},
                        host=cityqhd_host, dbname=cityqhd, upsert=True, **rx)

# upsert_roadxunjian()

def upsert_weixiu():
    weixiu, _ = m_util.m_list('bridge_repair', host=host, dbname=dbname, findall=True)
    for w in weixiu:
        m_util.m_update('bridge_repair', {'_id': ObjectId(w.pop('_id'))},
                        host=cityqhd_host, dbname=cityqhd, upsert=True, **w)

upsert_weixiu()

def upsert_roadweixiu():
    weixiu, _ = m_util.m_list('bridge_repair', host=host, dbname=dbname, findall=True)
    for w in weixiu:
        m_util.m_update('bridge_repair', {'_id': ObjectId(w.pop('_id'))},
                        host=cityqhd_host, dbname=cityqhd, upsert=True, **w)

upsert_roadweixiu()