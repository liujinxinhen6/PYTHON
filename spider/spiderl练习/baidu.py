import requests
keyword = input('请输入关键字:')
kw = {'wd':keyword}
try:
    r = requests.get('https://www.baidu.com/',params= kw)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("访问失败")

