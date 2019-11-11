import requests
import re
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

def get_HTTPpage():
    url = 'http://www.shuquge.com/txt/99462/index.html'
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        return response.text
    except:
        print("")


def getMessage():
    pat = '<a href="(\d+?).html">'
    data = re.compile(pat).findall(html)
    del data[0:12]
    return data


def getRead(st):
    try:
        response = requests.get(f'http://www.shuquge.com/txt/99462/{st}.html', headers=headers)
        response.encoding = response.apparent_encoding
        pat= '&nbsp;&nbsp;&nbsp;&nbsp;“(.*?)”'
        data = re.compile(pat).findall(response.text)
        return data
    except Exception as err:
        print(err)


if __name__ == '__main__':
    name = input('请入小说名称:')
    html = get_HTTPpage()
    ids = getMessage()
    f = open(name+'.txt', 'a')
    for id in ids:
        list = getRead(id)
        for i in range(0, len(list)):
            f.write(str(list[i]))
    f.close()
