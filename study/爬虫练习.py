import requests
url = 'https://item.jd.com/100006808184.html#none'
try:
	r = requests.get(url)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.text[:1000])
except:
	print('抓取失败')
