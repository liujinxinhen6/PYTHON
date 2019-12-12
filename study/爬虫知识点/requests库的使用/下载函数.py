#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/5 12:08
# @Author  : Liu jinxin
# @Github  : liujinxinhen6
# @File    : 下载函数.py
# @Function: 下载函数

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
def download(url, num_retries=2,proxies=None):
    try:
        response = requests.get(url, headers=headers, proxies=proxies)
        html = response.text
        if response.status_code >= 400:
            print('Download error:', response.text)
            html = None
            if num_retries and 500 <= response.status_code < 600:
                return download(url, num_retries-1)
    except requests.exceptions.RequestException as e:
        print('Download error:', e.reason)
        html = None
