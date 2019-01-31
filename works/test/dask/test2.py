# -*- coding:utf8 -*-
'''
这一步是要将亚马逊用户对音乐的评论从原始数据中提取出来，然后使用正则表达式将评论分词，
然后进行哈希映射将所有单词分配到100个文本文件中存储。相同的单词一定会被分配到同一个文件当中。
'''

#最后在找出100个文件中出现频率最高的1000个单词
import os
from collections import Counter
results = Counter()
for root, dirs, files in os.walk(r'F:/kaggle_dataset/亚马逊评论/制作亚马逊用户评论词云'):
    for file in files:
        with open(os.path.join(root, file)) as f:
            words_list = f.readlines()
            words_list = list(map(lambda x: x.strip('\n'),words_list))
            word_common_1000 = Counter(words_list).most_common(1000)
            results.update(word_common_1000)

#将每个文件中出现频率最高的1000个单词存入results当中。使用堆统计results当中出现频率最高的100单词。
import heapq
words_fren_list = list(results.keys())
words_fren_list_100 = heapq.nlargest(100,words_fren_list,key = lambda x:x[1])
len(words_fren_list_100)

word_frequence = {x[0]: x[1] for x in words_fren_list_100} #注意数据结构
'''
word_frequence
{'10': 11136,
'album': 140585,
'albums': 22047,
'amazing': 6245,
'artist': 5869,
'bad': 9842,
'band': 22550,
'bands': 4970,
'beat': 10468,
'beats': 7370,
'beautiful': 7736,
'bit': 8199,
'blues': 5310,
'buy': 7583,
'catchy': 5772,
'cd': 38605,
'classic': 13913,
'collection': 8004,
'dance': 5722}
'''
#下面使用WordCloud画出词云：
from wordcloud import WordCloud
import matplotlib.pyplot as plt
f, ax = plt.subplots(figsize=(7,4))
wordcloud = WordCloud(background_color='white',max_font_size=40,max_words=100,relative_scaling=.5).fit_words(word_frequence)
wordcloud.to_file("Amazonwordcloud.jpg")
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

