import requests

try:
    res = requests.get('https://www.amazon.cn/')
# print(res.status_code)
# print(res.encoding)
# print(res.apparent_encoding)
    res.raise_for_status()
    res.encoding = res.apparent_encoding
    print(res.text)
except:
    print('爬取失败')