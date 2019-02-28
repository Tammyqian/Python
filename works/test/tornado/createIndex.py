from mongo import MongoIns
m_util = MongoIns()
from kpages import srvtimer

def clear_data():
    m_util.m_createIndex('document', {'createTime5':1}, {'expireAfterSeconds': 5*60}, dbname='sjz', host='192.168.111.149:27011')

clear_data()
