#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
import time

# 创建一个类NextSecond()
class NextSecond():
    # 定义一个函数，实现将时间增加一秒的功能
    def next_second(self, str):
        # 匹配时间字符串中的所有数字，将其存为列表s_list
        s_list = re.findall('\d+', str)
        print s_list
        # 用于将序列中的元素以指定的字符连接生成一个新的字符串
        s = ''.join(s_list)
        print s
        # time.strptime()根据指定的格式把一个时间字符串解析为时间元组。
        strptime = time.strptime(s, "%Y%m%d%H%M%S")
        print strptime
        # time.mktime()函数会返回用秒数来表示时间的浮点数【时间戳】
        timestamp = time.mktime(strptime)
        print timestamp
        # 秒数加一
        new_timestamp = timestamp + 1
        # 再用time,localtime()函数作用是格式化时间戳为本地的时间
        new_str = time.localtime(new_timestamp)
        print new_str
        # 函数接收以时间元组,并返回以可读字符串表示的当地时间,格式由参数format决定。
        dt = time.strftime("%Y-%m-%d %H:%M:%S", new_str)
        print dt
        dt_list = re.findall("\d+", dt)
        print dt_list
        return "%s年%s月%s日%s时%s分%s秒" % (dt_list[0], dt_list[1], dt_list[2], dt_list[3], dt_list[4], dt_list[5])

if __name__ == '__main__':
    a = NextSecond()
    print a.next_second("2017年11月09日23时53分59秒")
    print a.next_second("2004年12月31日23时59分59秒")














