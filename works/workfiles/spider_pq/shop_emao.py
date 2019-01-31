import urllib
import json

import pandas as pd

from pyquery import PyQuery as pq
from tornado.httpclient import HTTPClient, HTTPRequest


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

    df = pd.DataFrame(lst, columns=['name','addr'])
    print url
    return  df

if __name__ == '__main__':

    dflst = None
    for i in range(1,428):
        df = get_data(i)
        if i>1:
            dflst =dflst.append(df)
        else:
            dflst = df


    dflst.to_csv('shop.emao.csv',encoding='utf-8')
    print('saved!')

