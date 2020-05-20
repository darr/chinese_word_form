#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : word_form.py
# Create date : 2019-08-08 14:29
# Modified date : 2020-05-20 22:18
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from pypinyin import lazy_pinyin
import os
import etc

class WordForm:
    def __init__(self, strokefile, radicalfile, char_dict):
        self.char_dict = char_dict
        self.stroke_dict = self._get_stroke_dict(strokefile)
        self.radical_dict = self._get_radical_dict(radicalfile)

    def _get_stroke_dict(self, strokefile):
        dic = {i.strip().split(':')[0]:[self.char_dict[j.split('/')[0]] for j in i.strip().split(':')[1].split(',')] for i in open(strokefile) if i.strip()}
        return dic

    def _get_radical_dict(self, radicalfile):
        dic = {i.strip().split(':')[0]:i.strip().split(':')[1] for i in open(radicalfile) if i.strip()}
        return dic

    def get_strokes(self, word):
        '''获取汉字笔画'''
        strokes = []
        chars = [c for c in word]
        for c in chars:
            stroke = ''.join(self.stroke_dict.get(c, c))
            strokes.append(stroke)
        return strokes

    def get_pinyin(self, word):
        '''获取汉字汉语拼音'''
        pinyins = lazy_pinyin(word)
        return pinyins

    def get_radical(self, word):
        '''获取汉字偏旁部首'''
        radicals = []
        chars = [c for c in word]
        for c in chars:
            stroke = self.radical_dict.get(c, c)
            radicals.append(stroke)
        return radicals

def test():
    word = '自然语言处理是皇冠上的一颗明珠'
    handler = WordForm(etc.STROKE_FILE_PATH, etc.RADICAL_FILE_PATH, etc.CHAR_DICT)
    strokes = handler.get_strokes(word)
    pinyins = handler.get_pinyin(word)
    radicals = handler.get_radical(word)

    print('strokes', strokes)
    print('pinyins', pinyins)
    print('radicals', radicals)

if __name__ == '__main__':
    test()
