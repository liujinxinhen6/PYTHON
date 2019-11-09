#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/9 22:39
# @Author  : Liu jinxin
# @Github  : liujinxinhen6
# @File    : urllib函数.py
# @Function: urllib基础
import urllib.request
path = ''
urllib.request.urlretrieve("https://wwww.baidu.com", path) # 下载网页内容
urllib.request.urlcleanup() #清除爬虫产生的内存
# info() 看网页相应的简介信息
data = urllib.request.urlopen('https://wwww.baidu.com', timeout=1) # 超时设置
print(data.info())
# getcode() 得到状态码
print(data.getcode())
# geturl() 得到当前页面的网页的url
print(data.geturl())




