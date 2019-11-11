#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 12:40
# @Author  : Liu jinxin
# @Github  : liujinxinhen6
# @File    : 构建IP代理池.py
# @Function: 构建IP代理池
# @Heraders: User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36

#
# import urllib.request
#
#
# ip = '1.198.111.109:9999'
# proxy = urllib.request.ProxyHandler({'https':ip})
# opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
# urllib.request.install_opener(opener)
# url = 'https://www.baidu.com/'
# data = urllib.request.urlopen(url).read().decode('utf-8')
# print(data)

import urllib.request
import random


ippool = [
    '112.247.66.254:9999',
    '112.247.100.200:9999',
    '112.247.5.22:9999'
]

#ip池
def getIp(ippool):
    thisip = random.choice(ippool)
    print(thisip)
    proxy = urllib.request.ProxyHandler({'http':thisip})
    opener = urllib.request.build_opener(proxy, urllib.request.ProxyHandler)
    urllib.request.install_opener(opener)
#ip接口