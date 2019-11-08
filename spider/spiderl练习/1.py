import requests
from bs4 import BeautifulSoup


r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo,"html.parser")# 对象和解析器,还有lxml xml html5lib
# print(soup.prettify())
# print(soup.title)
# tag = soup.a
# print(tag.attrs)
# print(tag.attrs['class'])
# print(tag.string)
# print(tag.comment)
print(soup.find_all('a'))