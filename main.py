#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : main.py
# Create date : 2019-08-08 14:26
# Modified date : 2019-08-22 11:53
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from word_form import WordForm
from build_radical import create_radicals

def query_text(word):

    print("句子：%s" % word)
    handler = WordForm()
    strokes = handler.get_strokes(word)
    pinyins = handler.get_pinyin(word)
    radicals = handler.get_radical(word)

    print('笔画：', strokes)
    print('拼音：', pinyins)
    print('偏旁部首：', radicals)
    print('\n')

def query():
    word = '自然语言处理是人工智能皇冠上的一颗明珠'
    query_text(word)
    word = '在技术上，深度学习技术会越来越强，新的语言模型和编码器也会越来越好。'
    query_text(word)
    word = '本项目是中文词语的笔画拆解，偏旁查询，拼音转换接口'
    query_text(word)
    word = '中文信息处理当中，语言外部形式上的特征在各个任务中扮演着越来越重要的角色'
    query_text(word)

def run():
    #create_radicals()
    query()

if __name__ == '__main__':
    run()
