#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 19:41
# @Author  : Liu jinxin
# @Github  : liujinxinhen6
# @File    : 1.4.py
# @Function: 1-n的平方和

def sums(n):
    sum = 0
    for i in range(1, n+1):
        sum = i*i + sum
    print(sum)

sums()
