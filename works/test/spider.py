# -*- coding:utf8 -*-

import urllib2
import requests
from lxml import etree
import time
from selenium import webdriver

driver = webdriver.Chrome()


def photoSpider():
    url = "http://sjz.thunics.com:9092/manage/road/xunjian/disease/list?start=2018-01-01&end=2018-11-05"
    req = urllib2.Request(url,headers={"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"})
    print url
    print req
    html = urllib2.urlopen(req).read()
    print html
    time.sleep(1)
    selector = etree.HTML(html)
    print selector

    # links = selector.xpath('//table/tbody/tr[1]/td[8]/span[0]/@imgurl')
    links = selector.xpath('//*[@id="table_sort"]/tbody/tr[0]/td[7]/span/@imgurl')
    print links

    for link in links:
        time.sleep(2)
        link = "http://sjz.thunics.com:9092" + link
        loadImages(link)

def loadImages(link):
    req = urllib2.Request(link,headers = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"})
    html = urllib2.urlopen(req).read()
    selector = etree.HTML(html)
    # 获取这个帖子里所有图片的src路径
    imagesLinks = selector.xpath('//img/@src')
    # 依次取出图片路径，下载保存
    for imagesLink in imagesLinks:
        writeImages(imagesLink)

def writeImages(imageLink):
    i = 1
    file = open('./images/','wb')
    images = requests.get(imageLink).read()
    file.write(images)
    file.close()
    i += 1

photoSpider()
