#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/15 10:39
# @Author  : Liu jinxin
# @Github  : liujinxinhen6
# @File    : 豆瓣电影.py
# @Function: 豆瓣电影
import requests
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    'Referer': 'https://www.douban.com/'
}

def get_page():
    try:
        url = 'https://movie.douban.com/cinema/nowplaying/shenzhen/'
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        data = response.text
        return data
    except Exception as err:
        print(err)


def prase_page(list,text):
    html = etree.HTML(text)
    title = html.xpath('//li[@class="list-item"]/@data-title')
    region = html.xpath('//li[@class="list-item"]/@data-region')
    for i in range(0, len(title)):
        list.append(title[i] + " : " + region[i])
    return list

    # for i in range (0,len(title)):
    #     print(title[i])
    #     # medium = title[i] + " : " +score[i]
    #     # message.append(medium)
    # print(message)


if __name__ == '__main__':
    list = []
    text = get_page()
    prase_page(list,text)
