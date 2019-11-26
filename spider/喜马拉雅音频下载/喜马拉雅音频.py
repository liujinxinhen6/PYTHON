#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 18:36
# @Author  : Liu jinxin
# @Github  : liujinxinhen6
# @File    : 喜马拉雅音频.py
# @Function: 喜马拉雅音频
import requests
import re
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}
def download(medium_name,medium_url):
    path = 'G:\喜马拉雅\无罪谋杀'
    response = requests.get(medium_url, headers = headers)
    with open(path + '\{}.mp4'.format(medium_name),'wb') as f:
        f.write(response.content)


def getmessage():
    trackId = []
    title = []
    for i in range(0,28):
        page = i+1
        response = requests.get('https://www.ximalaya.com/youshengshu/10587045/p' + str(page), headers = headers)
        data = response.text
        patid = 'href="/.*?/\d+/(\d{8})"'
        pattitle = '"isPaid":false,"tag":0,"title":"(.*?)","playCount"'
        mediumtitle = re.compile(pattitle).findall(data)
        mediumid = re.compile(patid).findall(data)
        for i in range(0,len(mediumid)):
            if mediumid[i] not in trackId:
                trackId.append(mediumid[i])
        for i in range(0, len(mediumtitle)):
            if mediumtitle[i] not in title:
                title.append(mediumtitle[i])
    return title,trackId

def get_api(trackId):
    api_url = 'https://www.ximalaya.com/revision/play/v1/audio?id='+trackId+'&ptype=1'
    r = requests.get(api_url, headers=headers)
    pat = '"src":"(.*?)",'
    medium_url = re.compile(pat).findall(r.text)
    return medium_url[0]

if __name__ == '__main__':
    message = getmessage()
    for i in range(0,len(message[0])):
        try:
            download(message[0][i],get_api(message[1][i]))
        except Exception as err:
            download('错误名称'+ str(i),get_api(message[1][i]))
            print(err)