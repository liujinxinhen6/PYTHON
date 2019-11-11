#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 13:35
# @Author  : Liu jinxin
# @Github  : liujinxinhen6
# @File    : 用户代理及ip代理糗事百科.py
# @Function: 用户代理及ip代理糗事百科
# @Heraders: User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36
import re
import urllib.request
import random


userpool = [
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12'
]
ippool = [
    '112.247.66.254:9999',
    '112.247.100.200:9999',
    '112.247.5.22:9999'
]


def getIpUser():
    user = random.choice(userpool)
    headers = ('User-Agent',user)
    ip = random.choice(ippool)
    proxy = urllib.request.HTTPHandler({'http':ip})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)



