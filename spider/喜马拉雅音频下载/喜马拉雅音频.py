#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 18:36
# @Author  : Liu jinxin
# @Github  : liujinxinhen6
# @File    : 喜马拉雅音频.py
# @Function: 喜马拉雅音频
import requests
from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}
def download(medium_name,medium_url):
    path = 'G:\喜马拉雅\无罪谋杀'
    response = requests.get(medium_url, headers = headers)
    with open(path + '\{}.mp4'.format(medium_name),'wb') as f:
        f.write(response.content)


def getmessage():
    response = requests.get('https://www.ximalaya.com/youshengshu/10587045/', headers = headers)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text,'html.parser')
    print(soup.prettify())
if __name__ == '__main__':
    getmessage()