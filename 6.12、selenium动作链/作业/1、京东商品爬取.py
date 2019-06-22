from selenium import webdriver
import time
import random

url="https://www.jd.com/"

driver=webdriver.Chrome()

driver.get(url)
time.sleep(2)

# 找到输入框，输入指定的字段
driver.find_element_by_xpath("//*[@id='key']").send_keys("笔记本")
time.sleep(2)

# 找到搜索按钮，模拟人点击
driver.find_element_by_xpath("//button[@class='button']").click()

for page in range(3):
    # 滑动窗口到底部
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
liList=driver.find_elements_by_xpath("//*[@id='J_goodsList']//li")
for i in liList:
    # 遍历每一个标签
    # 定位到标签后 使用.text获取文本信息
    price=i.find_element_by_xpath(".//div[@class='p-price']//i").text
    info=i.find_element_by_xpath(".//div[@class='p-name p-name-type-2']//em").text.replace("\n","")
    comment=i.find_element_by_xpath(".//div[@class='p-commit']/strong").text
    try:
        shop = i.find_element_by_xpath(".//div[@class='p-shop']/span/a").get_attribute("title")
    except:
        shop = "无"

    urls=i.find_element_by_xpath(".//div[@class='p-img']/a").get_attribute('href')

    print(price,info,comment,shop,urls)

driver.quit()



