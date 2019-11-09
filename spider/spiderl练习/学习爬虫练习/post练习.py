#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/9 23:41
# @Author  : Liu jinxin
# @Github  : liujinxinhen6
# @File    : post练习.py
# @Function: 
import urllib.request
import urllib.parse

posturl = 'https://www.iqianyue.com/mypost'
postdata = urllib.parse.urlencode({
    'name':'liujinxin',
    'pass':'asdasdasd'
}).encode('utf-8')
req = urllib.request.Request(posturl, postdata)
relt = urllib.request.urlopen(req).read().decode('utf-8')
f = open('post.html', 'a')
f.write(relt)
f.close()