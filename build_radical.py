#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : build_radical.py
# Create date : 2019-08-08 15:19
# Modified date : 2019-08-22 11:49
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from urllib import request
from lxml import etree
import chardet

def get_html(url):
    return request.urlopen(url).read().decode('gbk')

def create_radicals(): 
    #f = open('./data/radicals.txt', 'w+')
    f = open('radicals.txt', 'w+')
    start = 'http://xh.5156edu.com/bs.html'
    html = get_html(start)
    selector = etree.HTML(html)

    links = ['http://xh.5156edu.com/' + i for i in selector.xpath('//a[@class="fontbox"]/@href')]
    fonts = [i for i in selector.xpath('//a[@class="fontbox"]/text()')]
    font_dict = list(zip(fonts, links))
    for i in font_dict:
        w = i[0]
        link = i[1]
        html = request.urlopen(link).read().decode('GBK', 'ignore')
        selector = etree.HTML(html)
        words = [i for i in selector.xpath('//td/a[@class="fontbox"]/text()')]
        for wd in words:
            f.write(wd + ':' + w + '\n')
            print(w, wd)
    f.close()

def main():
    create_radicals()

if __name__=='__main__':
    main()
