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
        'code': 'bridgetype',
        'label': '结构类型',
    }
    m_util.m_update('options', {'code': 'bridgetype'}, dbname=cityqhd, host=cityqhd_host, upsert=True, **data)

def upsert_weixiu():
    weixiu, _ = m_util.m_list('bridge_repair', )


