import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText():
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    try:
        response = requests.get(url,timeout = 30)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        return response.text
    except:
        return "shibai"


def fillOrder(ulist, num):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])


def printOrder(ulist, num):
    geshi = "{0:{4}^10}\t{1:{4}^10}\t{2:{4}^10}\t{3:{4}^10}"
    print(geshi.format('排名', '学校', '城市', '总分',chr(12288)))
    for i in range(num):
        u = ulist[i]
        if u[1] == name:
            print("{0:{4}^10}\t{1:{4}^10}\t{2:{4}^10}\t{3:{4}^10}".format(u[0], u[1], u[2], u[3], chr(12288)))
        print("{0:{4}^10}\t{1:{4}^10}\t{2:{4}^10}\t{3:{4}^10}".format(u[0], u[1], u[2], u[3], chr(12288)))


if __name__ == '__main__':
    name = input('输入大学名称:')
    uinfo = []
    html = getHTMLText()
    fillOrder(uinfo,html)
    printOrder(uinfo,100)