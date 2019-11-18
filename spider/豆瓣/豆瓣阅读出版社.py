#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/9 21:17
# @Author  : Liu jinxin
# @Github  : liujinxinhen6
# @File    : 豆瓣阅读出版社.py
# @Function: 课后作业:打印豆瓣阅读出版社信息
import re
import urllib.request

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'

}
request = urllib.request.Request('https://read.douban.com/provider/all',headers=headers)
response = urllib.request.urlopen(request).read().decode("utf-8")
pat1 = '<div class="name">(.*?)</div><div class="works-num">(\d*?.*?)</div>'
cbmessage = re.compile(pat1).findall(response)
print(cbmessage)
f =open('豆瓣出版社信息.txt', 'a')
for i in range(0, len(cbmessage)):
    f.write(str(cbmessage[i]))
f.close()
