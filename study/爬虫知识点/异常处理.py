#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/9 23:57
# @Author  : Liu jinxin
# @Github  : liujinxinhen6
# @File    : 异常处理.py
# @Function: 异常处理

# URLError是HTTPError的父类
# URLRrror出现的原因:
# 1 连不上服务器
# 2 远程url不存在
# 3 无网络
# 4 触发HTTPError
# ...
import urllib.request
import urllib.error

try:
    data = urllib.request.urlopen('http://blog.csdn.net').read().decode('utf-8')
    print(data)
except urllib.error.URLError as e:
    if hasattr(e, 'code'):
        print(e.code)
    if hasattr(e, 'reason'):
        print(e.reason)