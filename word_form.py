#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : word_form.py
# Create date : 2019-08-08 14:29
# Modified date : 2019-08-22 11:48
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from pypinyin import lazy_pinyin
import os

class WordForm:
    def __init__(self):
        cur_dir = '/'.join(os.path.abspath(__file__).split('/')[:-1])
        strokefile = os.path.join(cur_dir, './data/strokes.txt')
        radicalfile = os.path.join(cur_dir, './data/radicals.txt')
        self.char_dict = {
            "点": "丶",
            "横": "一",
            "横钩": "乛",
            "横撇": "㇇",
            "横撇弯钩": "㇌",
            "横斜钩": "⺄",
            "横折": "𠃍",
            "横折竖钩": "㇆",
            "横折提": "㇊",
            "横折弯": "㇍",
            "横折弯钩": "㇈",
            "横折折": "㇅",
            "横折折撇": "㇋",
            "横折折折": "㇎",
            "横折折折钩": "𠄎",
            "捺": "㇏",
            "撇": "丿",
            "撇点": "𡿨",
            "撇折": "𠃋",
            "竖": "丨",
            "竖钩": "亅",
            "竖提": "𠄌",
            "竖弯": "㇄",
            "竖弯横钩": "乚",
            "竖折": "𠃊",
            "竖折撇": "ㄣ",
            "竖折折": "𠃑",
            "竖折折钩": "㇉",
            "提": "㇀",
            "弯钩": "㇁",
            "卧钩": "㇃",
            "斜钩": "㇂",
            }
        self.stroke_dict = {i.strip().split(':')[0]:[self.char_dict[j.split('/')[0]] for j in i.strip().split(':')[1].split(',')] for i in open(strokefile) if i.strip()}
        self.radical_dict = {i.strip().split(':')[0]:i.strip().split(':')[1] for i in open(radicalfile) if i.strip()}

    '''获取汉字笔画'''
    def get_strokes(self, word):
        strokes = []
        chars = [c for c in word]
        for c in chars:
            stroke = ''.join(self.stroke_dict.get(c, c))
            strokes.append(stroke)
        return strokes

    '''获取汉字汉语拼音'''
    def get_pinyin(self, word):
        pinyins = lazy_pinyin(word)
        return pinyins

    '''获取汉字偏旁部首'''
    def get_radical(self, word):
        radicals = []
        chars = [c for c in word]
        for c in chars:
            stroke = self.radical_dict.get(c, c)
            radicals.append(stroke)
        return radicals


def test():
    word = '自然语言处理是皇冠上的一颗明珠'
    handler = WordForm()
    strokes = handler.get_strokes(word)
    pinyins = handler.get_pinyin(word)
    radicals = handler.get_radical(word)

    print('strokes', strokes)
    print('pinyins', pinyins)
    print('radicals', radicals)

if __name__ == '__main__':
    test()
