#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 20:33
# @Author  : Liu jinxin
# @Github  : liujinxinhen6
# @File    : 递归之二分查找法.py
# @Function: 递归之二分查找法，如果知道数据顺序需要按从小到大来排放


def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high)/2
        if target < data[mid]:
            return binary_search(data, target, low, mid-1)
        elif target == data[mid]:
            return True
        else:
            return binary_search(data, target, mid+1, high)
