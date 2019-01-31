import pandas as pd

from pyquery import PyQuery as pq
from tornado.httpclient import HTTPClient, HTTPRequest
import dask

@dask.delayed
def get_data(pageindex):
    http_client = HTTPClient()
    url = 'http://shop.emao.com/list-0-0-0-0-{0}.html'.format(str(pageindex))
    resquest = HTTPRequest(url, method="GET")
    response = http_client.fetch(resquest)
    doc = pq(response.body)
    Remdetails = doc('.Remdetails')

    lst = []
    for item in Remdetails:
        _doc = pq(item)
        name = _doc('p').eq(0).text()
        addr = _doc('.Remsite').text()
        lst.append([name, addr])
    # print lst
    df = pd.DataFrame(lst, columns=['name','addr'])
    # print df, 'ffffffffff'
    print url
    return  df

def func(a):
    # print a
    return a

if __name__ == '__main__':

    dflst = []
    for i in range(1, 8):
        dflst.append(get_data(i))

    print dflst,'dddddddd',type(dflst)
    total = dask.delayed(func)(dflst)

    # print total, 'ttttttttt',type(total)
    result = total.compute()
    df = pd.concat(result)
    print 'aaaaaaa',df, 'ffffffff'
    # df = dask.compute(total)
    df.to_csv('shop.emao.csv',encoding='utf-8')
    print('saved!')
