import urllib.request
from mycodes import mycode


def getdata():
    data = urllib.request.urlopen('https://www.baidu.com').read().decode('utf-8')
    print(data)
    return data


if __name__ == '__main__':
    mycode.getopener()
    data = getdata()
    with open('1.html','w',encoding='utf-8')as f:
        f.write(data)
        f.close()

