import time
from mongo_util import MongoIns
m_util = MongoIns()
from datetime import datetime
def time_to_timestamp(strtime):
    timeArray = time.strptime(strtime, "%Y-%m-%d %H:%M:%S")
    timeStamp = time.mktime(timeArray)
def filter_time():
    t2 = time.localtime()
    print t2
    end = time.mktime(t2)
    print end
    start = str(t2.tm_year) + '0101000000'
    print start
    t1 = time.strptime(start,'%Y%m%d%H%M%S')
    print t1
    start = time.mktime(t1)
    print start
    t3 = datetime.fromtimestamp(start)
    t4 = datetime.fromtimestamp(end)
    print t3,t4,type(t3)
    cond = {'dtime': {'$gte': start, '$lt': end}}
    print cond
    # return m_util.m_update('document',dbname='sjz',host='192.168.111.5:27011',name = 'zhangsan',**cond)


filter_time()
# a = datetime.now()
# b = a.year
# b = a.replace(month=1,day=1,hour=0,minute=0,second=0).isoformat()
# print a,b
# c = datetime.now().isoformat()
# print c
# d = datetime(2015,1,1)
# print d,type(d)