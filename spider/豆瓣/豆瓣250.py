#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 9:59
# @Author  : Liu jinxin
# @Github  : liujinxinhen6
# @File    : 豆瓣250.py
# @Function: 豆瓣250
import re
import requests
import pymysql

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
def request_douban(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code==200:
            response.encoding = response.apparent_encoding
            return response.text
    except Exception as err:
        print(err)

def parse_html(html, list):
    num_pat = '<em class="">(\d+)</em>'
    title_pat = '<img width="100" alt="(.*?)"'
    date_pat = '<br>[\s]*(\d+)'
    introduce_pat = '<span class="inq">(.*?)</span>'
    link_pat = '<a href="(.*?)"[\s]*class="">'
    list['num_list'] = re.compile(num_pat).findall(html)
    list['title_list'] = re.compile(title_pat).findall(html)
    list['date_list'] = re.compile(date_pat).findall(html)
    list['introduce_list'] = re.compile(introduce_pat).findall(html)
    list['link_list'] = re.compile(link_pat).findall(html)
    return list


if __name__ == '__main__':
    list = {}
    conn = pymysql.connect(
        host='127.0.0.1',
        user='liujin',
        password='liujinxin',
        db='jinxin.com')
    for i in range(0,10):
        page = i*25
        url = 'https://movie.douban.com/top250?start=' + str(page) + '&filter='
        html = request_douban(url)
        parse_html(html, list)
        for i in range(0,len(list['num_list'])):
            try:
                num = list['num_list'][i]
                title = list['title_list'][i]
                date = list['date_list'][i]
                introduce = list['introduce_list'][i]
                link = list['link_list'][i]
                sql = "insert into doubanmovies(num,title,date1,introduce,link) values ('"+num+"','"+title+"','"+date+"','"+introduce+"','"+link+"')"
            except  Exception as err:
                print(err)
            try:
                conn.query(sql)
            except Exception  as err:
                print(err)
    conn.close()

