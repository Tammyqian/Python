# -*- coding:utf-8 -*-

# -------Dask解决方案-------#
import dask.bag as db
import ujson as json
# import json
import pandas as pd
import numpy as np
import gzip
import re

b = db.read_text(r'F:/kaggle_dataset/亚马逊评论/reviews_Digital_Music_5.json.gz', encoding='utf-8').map(json.loads)
b.take(1)
print(sum([1 for _ in gzip.open(r'F:/kaggle_dataset/亚马逊评论/reviews_Digital_Music_5.json.gz')]))  # 统计多少条数据
tempDir = 'F:/kaggle_dataset/亚马逊评论/制作亚马逊用户评论词云'
stopwords = set(pd.read_csv('C:/Users/zhangshuai_lc/stopwords_en.txt', header=None)[0])

pattern = re.compile(r'\w+')  # 正则


def hashFile():
    temp_path_list = []
    for i in range(1, 101):
        temp_path_list.append(open(tempDir + '/' + str(i) + '.txt', mode='w'))  # 构造100个文本文件路径
    for each in (gzip.open(r'F:/kaggle_dataset/亚马逊评论/reviews_Digital_Music_5.json.gz')):
        sentence = eval(each)  # 字符串转字典
        words = sentence['reviewText']
        words_list = pattern.findall(words)
        # print(words_list)
        for word in words_list:
            if word.lower() not in stopwords and len(word) >= 2:
                word = word.lower()
                temp_path_list[hash(word) % 100].write(word + '\n')  # 对单词进行hash，相同的单词一定会hash到同一个文件中
    for f in temp_path_list:
        f.close()


hashFile()