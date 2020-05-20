#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : etc.py
# Create date : 2020-05-20 22:06
# Modified date : 2020-05-20 22:21
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

import os

etc_path = os.path.abspath(__file__)
folder_path = os.path.dirname(etc_path)

STROKE_FILE_PATH = "%s/data/strokes.txt" % folder_path
RADICAL_FILE_PATH = "%s/data/radicals.txt" % folder_path

CHAR_DICT = {
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
