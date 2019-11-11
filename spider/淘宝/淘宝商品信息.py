from selenium import webdriver
import time
import re

# 选用谷歌浏览器
# driver = webdriver.Chrome()
# driver.get('https://www.taobao.com/')
# 找到元素,定位


def search_product():
    driver.find_element_by_xpath('//*[@id="q"]').send_keys(kw)
    driver.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button').click()
    time.sleep(20)
    token = driver.find_element_by_xpath('//*[@id="mainsrp-pager"]/div/div/div/div[1]').text
    token = int(re.compile('(\d+)').search(token).group(1))
    return token
# 强行阻止程序执行,停留10s
# 加载太慢会导致元素获取失败,需要下拉滑条
# 登录 下拉 采集数据 下一页 循环


def dropdown():
# 一次拉一点,要暂停一段时间
    for x in range(1,11,2):
        time.sleep(0.5)
        j = x/10
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)
# j代表位置


def get_product():
# 获取所有的div,遍历div,再在div里面寻找文件
    divs = driver.find_elements_by_xpath('//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')
    for div in divs:
        info = div.find_element_by_xpath('.//div[@class="row row-2 title"]').text
        image = div.find_element_by_xpath('.//div[@class="pic"]/a/img').get_attribute('src')
        deal = div.find_element_by_xpath('.//div[@class="deal-cnt"]').text
        price = div.find_element_by_xpath('.//a[@class="J_ClickStat"]').get_attribute('trace-price') + '元'
        location = div.find_element_by_xpath('.//div[@class="row row-3 g-clearfix"]/div[@class="location"]').text
        name = div.find_element_by_xpath('.//div[@class="shop"]/a/span[2]').text
        product = {'标题':info,'价格':price,'订单量':deal,'图片':image,'名字':name,'位置':location}
        print(product)


def next_page():
    token = search_product()
    dropdown()
    get_product()
    num = 1
    while num != token:
        driver.get('https://s.taobao.com/search?q={}&s={}'.format(kw,num*44))
        num += 1
        # time.sleep(4)
        driver.implicitly_wait(10)  # 隐式等待最高等待时间为10s
        dropdown()
        get_product()


if __name__ == '__main__':
    kw = input('请输入您想要搜索的商品: ')
    driver = webdriver.Chrome()
    driver.get('https://www.taobao.com/')
    next_page()
