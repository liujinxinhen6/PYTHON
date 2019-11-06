import re
import requests

url = 'https://wenku.baidu.com/search?'
session = requests.session()
r = session.get(url)
print(r.text)


