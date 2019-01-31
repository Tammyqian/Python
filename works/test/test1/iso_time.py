import time
from datetime import datetime
from mongo_util import MongoIns

t1 = time.time()
t2 = t1 - 365*24*3600*10
start = datetime.fromtimestamp(t2)
end = datetime.fromtimestamp(t1)
cond = {'dtime':{'$gt':start,'$lt':end}}

fields = dict(dtime=1,node_id=1)
tlist, _ = MongoIns().m_list('data_AnemometerHCF900',dbname='qa-test',host='192.168.111.149:27019',fields=fields,findall='1',**cond)
print tlist