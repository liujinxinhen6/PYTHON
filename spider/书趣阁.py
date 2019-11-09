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
    # ples = re.findall('\d\d\d\d\d\d\d\d.html', html)

    # print(ples)





def getRead(st):
    response = requests.get(url=f"http://www.shuquge.com/txt/99462/{st}", headers=headers)
    response.encoding = response.apparent_encoding
    b = response.text
    print(b)


if __name__ == '__main__':
    html = get_HTTPpage()
    getMessage()

