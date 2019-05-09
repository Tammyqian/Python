# -*- coding:utf-8 -*-

from mongo_util import MongoIns
m_util = MongoIns()
from pymongo import MongoClient
client = MongoClient()

host = '192.168.111.5:27011'
dbname = 'lijiakui_web'

client = MongoClient(host='192.168.111.5', port=27011)
print client
collection = client.lijiakui_web.document
print collection

cond = [
    {'item': "card", 'qty': 15},
    {'item': "envelope", 'qty': 20},
    {'item': "stamps", 'qty': 30}
]
# print m_util.m_insert('document', dbname=dbname, host=host, data={'item': "stamps", 'qty': 30})
# print _id
m_util.m_insert('document', dbname=dbname, host=host, gongdan=False, name='zhang')

# collection.insert([{'item': "card", 'qty': 15},{'item': "envelope", 'qty': 20},{'item': "stamps", 'qty': 30}])


