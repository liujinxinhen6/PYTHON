#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/14 22:18
# @Author  : Liu jinxin
# @Github  : liujinxinhen6
# @File    : 淘宝信息测试.py
# @Function: 淘宝信息测试
# @Heraders: User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36
import requests
import re
import json
headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Cookie': "alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; cookie2=103de9a55c74c5170c9062252da4df6b; t=7ba36f96f990b8a6868d82d4e86c8a3a; _tb_token_=f33e37ef383ee; cna=MqxSFtb01jcCAduFnzkwQwTx; v=0; uc3=nk2=lWlJPLI1joqO2A%3D%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D&vt3=F8dByuWkz5%2F1g%2Blvo38%3D&id2=UUGhbsK9jtCRSg%3D%3D; csg=16cabf0c; lgc=%5Cu946B%5Cu60F3%5Cu4E8B%5Cu621073; dnk=%5Cu946B%5Cu60F3%5Cu4E8B%5Cu621073; skt=f714c1b3c8eaed97; existShop=MTU3Mzc0NDEwMA%3D%3D; uc4=id4=0%40U2OW7P%2BlfhutDvrJtSg3H%2BYaolxN&nk4=0%40l5ucsiTOhupTAwzO82%2FqCQVOmJnA; tracknick=%5Cu946B%5Cu60F3%5Cu4E8B%5Cu621073; _cc_=U%2BGCWk%2F7og%3D%3D; tg=0; enc=4oIr%2FL7j2XIfLaZJX1LNwEadIbX1R1uZLrSck90MOSJoknaiONn0uuucN4Wl0WsrQ58qe%2FwygA7izkGvu7mcLQ%3D%3D; mt=ci=33_1; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; JSESSIONID=327ED09C0DD62BF67BFE75E1A8B3EBF3; uc1=cookie15=UIHiLt3xD8xYTw%3D%3D&cookie14=UoTbnr%2FWuYFlMw%3D%3D; isg=BFxc5yTObaE1Jxn4IvwHy9RoLXoO1QD_uoqv1TZc6scqgf4LWOXQj9Jz5el5DjhX; l=dB_i9eYcqeD9R9BDBOfZlurza77OrIObz1PzaNbMiICPO_1M5osCWZde1IYHCnGVHshpS3P5zp3_BcYF5yCqJxpswAaZk_DmndC.."
}



def get_taobao(url):
    try:
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        data = response.text
        if response.status_code == 200:
            print(data.json())
            return data # json转码问题
    except Exception as err:
        print(err)









if __name__ == '__main__':
    name = input('输入商品名称:')
    page = input('获取页数:')
    i = (int(page)-1)*44
    url = 'https://s.taobao.com/search?q='+name+'&s='+ str(i)
    get_taobao(url)

