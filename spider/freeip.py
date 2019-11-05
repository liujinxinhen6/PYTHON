import requests
from bs4 import BeautifulSoup

with open('ip.text', 'a', encoding='utf-8') as f:
    for page in range(1,10):
        url = 'https://www.xicidaili.com/nn' + '/'+ str(page)
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        r = requests.get(url,headers=headers) # 检测爬虫,需要伪装!
        html = r.text
        soup = BeautifulSoup(html,'lxml')
        all = soup.find_all('tr',class_='odd')
# print(all)

    for i in all:
        t = i.find_all('td')
        ip = t[1].text + ':' + t[2].text
        place = t[3].text
        print(ip,place)
        proxies = {'http': 'http://' + ip, 'https':'https://' + ip}
            # 验证有效性
        testurl = 'https://www.baidu.com/'
        try:
            r = requests.get(testurl, proxies=proxies, headers=headers, timeout=5).status_code
            if r == 200:
                f.write(ip+'\n')
                print(ip)
                print('ip可用')
        except:
            print('ip无效')

# 保存数据
