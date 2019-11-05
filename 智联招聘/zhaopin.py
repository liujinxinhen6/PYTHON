import requests


def getJsonDate():
    url = 'https://hm.baidu.com/hm.gif?cc=1&ck=1&cl=24-bit&ds=1536x864&vl=656&ep=344.5*106*21*64*0*%23rightNav_top%3Ediv%3Ediv%5B2%5D%3Ediv%3Ediv%3Ediv%5B2%5D%3Ediv%3Ediv%3Ea*97*56*a*&et=2&ja=0&ln=zh-cn&lo=0&rnd=993589648&si=38ba284938d5eddca645bb5e02a02006&v=1.2.63&lv=1&sn=50429'
    response = requests.get(url)
    return response.json()



if __name__ == '__main__':
    result = getJsonDate()
    print(result)