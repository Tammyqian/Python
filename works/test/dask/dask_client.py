# -*- coding: utf-8 -*-
from dask.distributed import Client
# client = Client("192.168.3.145:8786")
client = Client("192.168.3.167:8786")
import time
import dask.dataframe as dd
import json
from mongo import MongoIns

DB_HOST = "192.168.111.9:27017"


def square(x):
    print "正在阅读csv",str(x)*20
    df = dd.read_csv("/Users/yangxiao/works/sjfx/20180203.csv")
    columns = df.columns.tolist()[0:113]
    df = df.loc[:, columns]
    dmap = dict()
    for c in columns:
        if '\t' in c:
            nc = str.replace(c, '\t', '')
            dmap[c] = nc.strip()
    df = df.compute()
    df.rename(columns=dmap, inplace=True)
    result = json.loads(df.to_json(orient='records'))
    print result[0]


_start = int(time.time())

A = client.map(square, range(5))
for index, i in enumerate(A):
    print i.result()
    print "当前个数",index

_end = int(time.time())
print "总耗时{}秒".format(_end-_start)
