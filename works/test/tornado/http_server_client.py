from tornado.httpclient import HTTPRequest, HTTPClient, AsyncHTTPClient
import pandas as pd
from pyquery import PyQuery as pq
# import pandas as pd
from tornado import gen
import tornado

def get_http():
    http_client = HTTPClient()
    response = http_client.fetch("http://shop.emao.com/list-0-0-0-0-1.html")
    print response.body,type(response.body)

    doc = pq(response.body)
    Remdetails = doc(".Remdetails")
    print Remdetails
    lst = []
    for item in Remdetails.items():
        name = item("p").eq(0).text()
        # name = item('h6 p').text()
        addr = item(".Remsite").text()
        lst.append([name,addr])

    df = pd.DataFrame(lst, columns=['name', 'addr'])
    return df

@gen.coroutine
def get_asynchttp():
    http_client = AsyncHTTPClient()
    url1 = "http://shop.emao.com/list-0-0-0-0-1.html"
    url2 = "http://shop.emao.com/list-0-0-0-0-2.html"
    url3 = "http://shop.emao.com/list-0-0-0-0-3.html"
    url4 = "http://shop.emao.com/list-0-0-0-0-4.html"

    response1, response2 = yield [http_client.fetch(url1),http_client.fetch(url2)]
    response_dict = yield dict(response3=http_client.fetch(url3),
                               response4=http_client.fetch(url4))
    print response1.body
    response3 = response_dict['response3']
    response4 = response_dict['response4']


if __name__ == '__main__':
    # print get_http()
    res = get_asynchttp()











