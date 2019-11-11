#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/10 20:37
# @Author  : Liu jinxin
# @Github  : liujinxinhen6
# @File    : 用户池构建.py
# @Function: 用户池构建
# @Heraders: User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36

import re
import urllib.request
import random


userpool = [
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12'
]


def getUser(userpool):
    thisuser = random.choice(userpool)
    headers = ('User-Agent', thisuser)
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    #安装为全局
    urllib.request.install_opener(opener)

def getData(page):
    url = "http://www.lovehhy.net/Joke/Detail/QSBK/"+str(page)
    data = urllib.request.urlopen(url).read().decode('UTF-8', 'ignore')
    pat = '<div id="endtext">.*?(.*?)<br />.*?<br /><br /><br /></div>'
    list = re.compile(pat).findall(data)
    return list


if __name__ == '__main__':
    getUser(userpool)
    for i in range(1, 10):
        text = getData(i)
        for j in range(0, len(text)):
            print(text[i])
            print('-------')



