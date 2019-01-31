import urllib
import json
import pandas as pd

from tornado.httpclient import HTTPClient, HTTPRequest


def get_data(pageindex):
    http_client = HTTPClient()
    url = 'https://leaseconsumer.souche.com//v1/followShopApi/getShopPage.json'
    args = dict(page=pageindex, pageSize=100)
    body = urllib.urlencode(args)
    resquest = HTTPRequest(url, method="POST", body=body)
    response = http_client.fetch(resquest)
    # print response.body
    res = json.loads(response.body, encoding='utf-8')
    df= pd.DataFrame(res['data']['items'])
    return df

if __name__ == '__main__':
    dflst = None
    for i in range(1,48):
        df = get_data(i)
        if i>1:
            dflst =dflst.append(df)
        else:
            dflst = df


    dflst.to_csv('shop.csv',encoding='utf-8')
    print('saved!')

