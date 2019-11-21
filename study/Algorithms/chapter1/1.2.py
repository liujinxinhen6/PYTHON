#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 17:47
# @Author  : Liu jinxin
# @Github  : liujinxinhen6
# @File    : 1.2.py
# @Function: 用位运算通过位运算来判断一个数是否是偶数 将一个十进制整数转换为2进制数因为2进制数的高位都是
# 2的整次幂所以这个数是否是偶数取决于低位如果低位是0 则为偶数 如果低位是1则为奇数
# 1是001 2是010则发现如果是奇数与1相与后必定是001 如果是偶数必定是000



def is_even(k):
    if k&1 == 1:
        print(False)
    else:
        print(True)
is_even(8)
