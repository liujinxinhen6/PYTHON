#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 19:35
# @Author  : Liu jinxin
# @Github  : liujinxinhen6
# @File    : 1.3.py
# @Function: 1.3


def minmax(data):
    min = data[0]
    max = data[0]
    for num in data:
        if min > num:
            min = num
        if max < num:
            max = num
    print(max)
    print(min)

data = (1,2,34,43,23)
minmax(data)