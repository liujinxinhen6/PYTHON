from selenium import webdriver


def getHTTPtext():
    driver.find_element_by_xpath('/html/body/div[5]/dl/dd[13]/a').click()
    message = driver.find_element_by_xpath('//*[@id="content"]').text
    return message


def nexttext():
    driver.find_element_by_xpath('//*[@id="wrapper"]/div[4]/div[2]/div[3]/ul/li[3]/a').click()
    message = driver.find_element_by_xpath('//*[@id="content"]').text
    return message


if __name__ == '__main__':
    name = input('请输入小说名字:')
    num = int(input('下载页数:'))
    driver = webdriver.Chrome()
    driver.get("http://www.shuquge.com/txt/5809/index.html")
    first = getHTTPtext()
    f = open(name+'.txt', 'a')
    f.write(first)
    for i in range(1, num):
        next = nexttext()
        f.write(next)
    f.close()

