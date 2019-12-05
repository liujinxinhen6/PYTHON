#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/5 10:47
# @Author  : Liu jinxin
# @Github  : liujinxinhen6
# @File    : 重试下载.py
# @Function: 重试下载

import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError

def download(url, num_retries=2):
    print('Downloading:', url)
    try:
        html = urllib.request.urlopen(url).read()
        print(html)
    except (URLError, HTTPError, ContentTooShortError) as e:
        print("download error:", e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 < e.reason < 600:
                # retry 5xx 的返回网页
                return download(url, num_retries - 1)
        return html

if __name__ == '__main__':
    download(url = 'https://www.baidu.com', num_retries=2)