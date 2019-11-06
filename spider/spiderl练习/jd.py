import requests

res = requests.get('https://www.jd.com')
# print(res.status_code)
# print(res.encoding)
# print(res.text)
res.encoding = res.apparent_encoding
print(res.text)