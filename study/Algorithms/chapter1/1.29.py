#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 21:06
# @Author  : Liu jinxin
# @Github  : liujinxinhen6
# @File    : 1.29.py
# @Function: 1.29
def change(charactes,i,j):
    temp=characters[i]
    characters[i]=characters[j]
    characters[j]=temp
def permutation(characters,begin,end):
    str=''
    if(begin==end):
        for character in characters:
            str+=character
        print(str)
    else:
        for i in range(begin,end+1):
            change(characters,i,begin)
            permutation(characters,begin+1,end)
            change(characters, i,begin)
characters=['c','a','t','d','o','g']
permutation(characters,0,5)
