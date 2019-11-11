#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/10 13:31
# @Author  : Liu jinxin
# @Github  : liujinxinhen6
# @File    : 博客首页文章.py
# @Function: 博客首页文章
import urllib.request
import re

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.6'
}


def getPageHTTP():
    try:
        url = 'https://blog.csdn.net/'
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request).read().decode('utf-8', 'ignore')
        print(response)
        return response
    except Exception as err:
        print(err)


def gethttpList():
    pat = '<a href="(.*?)" target="_blank"'
    list = re.compile(pat).findall(html)
    return list


if __name__ == '__main__':
    html = getPageHTTP()
    httplist = gethttpList()
    for i in range(0,len(httplist)):
        print(httplist[i])
        urllib.request.urlretrieve(httplist[i], "E:\\PYTHON\\PYTHON\\spider\\spiderl练习\\学习爬虫练习\\" + str(i) + ".html")
