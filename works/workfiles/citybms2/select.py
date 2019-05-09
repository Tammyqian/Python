# -*- coding:utf-8 -*-

import os, time
from multiprocessing import Pool

from bson import ObjectId
from mongo_util import MongoIns
m_util = MongoIns()
from define import *
from roaddefine import *
from pymongo import MongoClient

host = '192.168.111.5:27011'
dbname = 'sjz'

cityqhd = 'cityqhd'
cityqhd_host = '121.22.33.134:27017'

cas = 'cas'
cas_host = '192.168.111.149:27017'


def getXunjProject():
    mapXunjProject = []
    for item in XUNJIAN_PROJECT:
        mapXunjProject.append({item[0]: item[1]})
    data = {
        'options': mapXunjProject,
        'code': 'bridgexunjproject',
        'label': '桥梁检查项目'
    }
    m_util.m_update('options', {'code': 'bridgexunjproject'}, dbname=cityqhd, host=cityqhd_host, upsert=True, **data)

    mapRoadXunjProject = []
    for item in ROAD_XUNJIAN_PROJECT:
        mapRoadXunjProject.append({item[0]: item[1]})
    data = {
        'options': mapRoadXunjProject,
        'code': 'roadxunjproject',
        'label': '道路检查项目'
    }
    m_util.m_update('options', {'code': 'roadxunjproject'}, dbname=cityqhd, host=cityqhd_host, upsert=True, **data)
# getXunjProject()


def mapInfo():
    options, _ = m_util.m_list('options', host=host, dbname=dbname, findall=True)
    for p in options:
        m_util.m_update('options', {'_id': ObjectId(p.pop('_id'))},
                        host=cityqhd_host, dbname=cityqhd, upsert=True, **p)

# mapInfo()

def upsert_fsfiles():
    client_host, client_port = cityqhd_host.split(':')
    client = MongoClient(host=client_host, port=int(client_port))
    tb = client[cityqhd]['fs.files']

    data = tb.find({}).sort([('_id', -1)]).limit(1)
    data = list(data)
    if data:
        _id = data[0].get('_id', '')
    else:
        data = m_util.m_find_one('fs.files', host=host, dbname=dbname)
        _id = data.get('_id')
    print _id
    # fs_chunks, _ = m_util.m_list('fs.chunks', host=host, dbname=dbname, findall=True)

    imgType = ['application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'application/octet-stream']
    while True:
        fids, _ = m_util.m_list('fs.files', host=host, dbname=dbname, findall=True, contentType={'$nin': imgType},
                                page_size=1000, _id={'$gte': ObjectId(_id)}, sorts=[('_id', 1)])

        last_id = _id
        for f in fids:
            if f.get('_id') > last_id:
                last_id = f['_id']
            m_util.m_update('fs.files', {'_id': ObjectId(f.pop('_id'))},
                        host=cityqhd_host, dbname=cityqhd, upsert=True, **f)

            fs_chunks, _ = m_util.m_list('fs.chunks', host=host, dbname=dbname,
                                         findall=True, files_id=ObjectId(last_id))
            for chunks in fs_chunks:
                if not chunks: continue
                m_util.m_update('fs.chunks', {'_id': ObjectId(chunks.pop('_id'))},
                            host=cityqhd_host, dbname=cityqhd, upsert=True, **chunks)

        if len(fids) < 1000:
            break
        else:
            _id = last_id

start = time.time()
print 'start: ', start
upsert_fsfiles()
end = time.time()
print 'end: ', end
print 'end - start: ', end - start
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(20)
#     start = time.time()
#     for i in range(20):
#         p.apply_async(upsert_fsfiles)
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     end = time.time()
#     print 'end - start: ', end - start
#     print('All subprocesses done.')
