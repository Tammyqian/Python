# -*- coding:utf-8 -*-

import pandas as pd
import urllib2
from tornado.httpclient import HTTPClient,HTTPRequest
import json, re
def download_data(index):
    # http_client = HTTPClient()
    url = 'https://webapi.daikuan.com/api/ExperienceStore/GetStoreList?' \
          'callback=jQuery112406491876852576828_1550660434711&pageIndex={}' \
          '&pageSize=150&provinceId=0&cityId=0'.format(index)
    # url = urllib2.Request(url)
    response = urllib2.urlopen(url).read()

    # url = HTTPRequest(url, method='GET')
    # res = http_client.fetch(url)
    # print res.body,'rrrr'

    # response 与 res.body 等效
    jsondata = re.search(r'\(([\s\S]*?)$', response).group(1)[:-1]
    print jsondata
    jsondata = json.loads(jsondata)
    # lst = []
    # for item in jsondata['Data']:
    #     name = item['Name']
    #     addr = item['Address']
    #     lst.append([name, addr])
    # print lst
    # print len(lst)
    # return lst
    return jsondata

if __name__ == '__main__':
    lst = []
    for i in range(1,3):
        jsondata = download_data(i)
        for item in jsondata['Data']:
            name = item['Name']
            addr = item['Address']
            lst.append([name, addr])
    print lst
    print len(lst)
    df = pd.DataFrame(lst, columns=['name', 'addr'])
    df.to_csv('daikuan2.csv', encoding='utf-8')


