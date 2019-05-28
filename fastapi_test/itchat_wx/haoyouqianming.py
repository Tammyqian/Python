# coding:utf-8
import itchat
import re
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import PIL.Image as Image
import os
import numpy as np

itchat.login()
friends = itchat.get_friends(update=True)[0:]

def get_sign():
    for i in friends:
        signature = i['Signature']
        print(signature)

def get_signature():
    for i in friends:
        signature = i['Signature'].strip().replace('span','').replace('class', '').replace('emoji', '')
        rep = re.compile('1f\d.+')
        signature = rep.sub('', signature)
        print(signature)

def jieba_signature():
    tList = []
    for i in friends:
        signature = i['Signature'].replace(' ', '').replace('span', '').replace('class', '').replace('emoji', '')
        rep = re.compile('1f\d.+')
        signature = rep.sub('', signature)
        tList.append(signature)

    text = ''.join(tList)
    wordlist_jieba = jieba.cut(text, cut_all=True)
    wl_space_split = ' '.join(wordlist_jieba)

    my_wordcloud = WordCloud(background_color="white", max_words=2000,
                             max_font_size=40, random_state=42,
                             font_path='/usr/share/fonts/msyh.ttf').generate(wl_space_split)
    plt.imshow(my_wordcloud)
    plt.axis('off')
    plt.show()


def jieba_signature2():
    tList = []
    for i in friends:
        signature = i['Signature'].replace(' ', '').replace('span', '').replace('class', '').replace('emoji', '')
        rep = re.compile('1f\d.+')
        signature = rep.sub('', signature)
        tList.append(signature)

    text = ''.join(tList)
    wordlist_jieba = jieba.cut(text, cut_all=True)
    wl_space_split = ' '.join(wordlist_jieba)

    d = os.path.dirname(__file__)
    print(d)
    alice_coloring = np.array(Image.open(os.path.join(d, 'wechat.jpg')))
    my_wordcloud = WordCloud(background_color='white', max_words=2000, mask=
                             alice_coloring,max_font_size=40,random_state=42,
                             font_path='/usr/share/fonts/msyh.ttf').generate(wl_space_split)
    image_colors = ImageColorGenerator(alice_coloring)
    plt.imshow(my_wordcloud.recolor(color_func=image_colors))
    plt.imshow(my_wordcloud)
    plt.axis('off')
    plt.show()

    my_wordcloud.to_file(os.path.join(d,'wechat_cloud.png'))
    itchat.send_image('wechat_cloud.png', 'filehelper')


if __name__ == '__main__':
    get_sign()
    get_signature()
    jieba_signature()
    jieba_signature2()
