from selenium import webdriver
import time

#定义url
url="https://www.guazi.com/zz/buy/"

#确定浏览器
driver=webdriver.Chrome()

#打开url
driver.get(url)

# 一定记得加s 得到多个车的信息列表
liList=driver.find_elements_by_xpath('//li[@data-scroll-track]')
print(len(liList))

time.sleep(1)

for i in liList:
    print(i)
    print(type(i))
    shape=i.find_element_by_xpath('.//h2[@class="t"]').text
    year=i.find_element_by_xpath('.//div[@class="t-i"]').text
    price=i.find_element_by_xpath('//div[@class="t-price"]/p').text
    print(shape,year,price)


driver.quit()