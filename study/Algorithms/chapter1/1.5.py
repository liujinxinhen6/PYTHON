#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 19:45
# @Author  : Liu jinxin
# @Github  : liujinxinhen6
# @File    : 1.5.py
# @Function: 放在列表里直接加起来

def sums(n):
    list = []
    for i in range(1, n+1):
        a = i*i
        list.append(a)
    print(sum(list))

sums(2)
