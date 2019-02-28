import time
from mongo_util import MongoIns; m_util = MongoIns()
import random
from multiprocessing import Pool
import os
from datetime import datetime

def a(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    for i in range(100000):
        data = {str(k):v for k,v in enumerate([random.random() for i in range(20)])}
        # data['dtime'] = datetime.fromtimestamp(time.time()) # localtime
        data['dtime'] = datetime.utcfromtimestamp(time.time()) # utc time
        m_util.m_insert('document', host='192.168.111.5:27011', dbname='sjz', **data)


def main():
    print('Parent process %s.' % os.getpid())
    p = Pool(20)
    for i in range(20):
        p.apply_async(a, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

def del_data():
    start = time.time()
    print "start {}".format(start)
    m_util.m_del('document', host='192.168.111.5:27011', dbname='sjz')
    end = time.time()
    print "end {}".format(end)
    print "end - start = {}".format(end - start)


import pymongo

def createIndex():
    # client = pymongo.MongoClient(host='192.168.111.5', port=27011)
    # collection = client['sjz']['document']
    # # collection.insert({'title':'test'})
    # collection.create_index([('dtime', 1)], expireAfterSeconds=120)
    print 'start', time.time()
    m_util.get_conn(host='192.168.111.5:27011')['sjz']['document'].create_index([('dtime', 1)], expireAfterSeconds=600)
    print 'end', time.time()

if __name__ == '__main__':
    # a('test')
    # main()
    # del_data()
    createIndex()

