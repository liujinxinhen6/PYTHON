#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 17:04
# @Author  : Liu jinxin
# @Github  : liujinxinhen6
# @File    : XPath表达式.py
# @Function: XPath表达式
# @Heraders: User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36
# @Ip      : 192.168.1.123

#
# / 逐层提取
# text()提取标签下的文本
# //标签名**提取所有**的标签
# //标签名[@属性='属性值']  提取属性为xx的标签
#@代表取某个属性
#
#
# 实列:
# 提取标题:
# /html/head/title/trxt()
# 提取所有div标签:
# //div
# 提取div中某个标签的内容:
# //div[@class='tools']