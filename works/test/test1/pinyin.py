#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    Author:cleverdeng
    E-mail:clverdeng@gmail.com
"""

__version__ = '0.9'
__all__ = ["PinYin"]

import os.path


class PinYin(object):
    def __init__(self, dict_file='word.data'):
        self.word_dict = {}
        self.dict_file = dict_file
        self.load_word()

    def load_word(self):
        if not os.path.exists(self.dict_file):
            raise IOError("NotFoundFile")

        with file(self.dict_file) as f_obj:
            for f_line in f_obj.readlines():
                try:
                    line = f_line.split('    ')
                    self.word_dict[line[0]] = line[1]
                except:
                    line = f_line.split('   ')
                    self.word_dict[line[0]] = line[1]

    def hanzi2pinyin(self, string=""):
        result = []
        if not isinstance(string, unicode):
            string = string.decode("utf-8")

        for char in string:
            key = '%X' % ord(char)
            result.append(self.word_dict.get(key, char).split()[0][:-1].lower())

        return result

    def pinyin(self, string=""):
        """
            汉字转拼音首字母
        """
        result = []
        if not isinstance(string, unicode):
            string = string.decode("utf-8")

        for char in string:
            key = '%X' % ord(char)
            if self.word_dict.get(key, char).split()[0][:-1]:
                result.append(self.word_dict.get(key, char).split()[0][:-1].lower())

        return ''.join(result)

    def simplepinyin(self, string=""):
        """
            汉字转拼音首字母 首字母
        """
        result = []
        if not isinstance(string, unicode):
            string = string.decode("utf-8")

        for char in string:
            key = '%X' % ord(char)
            if self.word_dict.get(key, char).split()[0][:-1]:
                result.append(self.word_dict.get(key, char).split()[0][:-1].lower()[0])

        return ''.join(result)


if __name__ == "__main__":
    string = "联调测试大桥abc"
    print PinYin().hanzi2pinyin(string)
    print PinYin().pinyin(string)
    print PinYin().simplepinyin(string)

