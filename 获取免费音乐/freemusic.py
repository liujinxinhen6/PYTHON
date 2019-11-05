from selenium import webdriver
import requests
import json
import  re
from urllib.request import urlretrieve
# qqmusic 爬虫接口 www.douqq.com/qqmusic

def get_url():
    url = 'https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w={}'.format(name)

    driver.get(url)
    driver.implicitly_wait(5)
    data = driver.find_element_by_xpath('//*[@id="song_box"]/div[2]/ul[2]/li[1]/div/div[2]/span[1]/a').get_attribute('href')
    print(data)
    data = {'mid':data}
    return data


def get_music_url(data):
    url = 'http://www.douqq.com/qqmusic/qqapi.php'
    req = requests.post(url, data=data).text
    req = json.loads(req)
    req = req.replace('\/\/', '//').replace('\/','/')
    print(req)
    rg = re.compile('"mp3_h":"(.*?)",')
    rs = re.findall(rg, req)[0]
    return rs

def get_music(rs):
    urlretrieve(rs,name + ".mp3")



def go():
    data = get_url()
    rs = get_music_url(data)
    get_music(rs)


if __name__ == '__main__':
    name = input('请输入你想要下载的歌曲:')
    driver = webdriver.Chrome()
    go()