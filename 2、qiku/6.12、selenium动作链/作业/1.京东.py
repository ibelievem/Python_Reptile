from selenium import webdriver
from time import sleep
import random

driver = webdriver.Chrome()
driver.get("https://www.jd.com/")

key = driver.find_element_by_id("key")
key.send_keys("笔记本电脑")
sleep(1)
searchBtn = driver.find_element_by_xpath("//button[@class='button']")
searchBtn.click()

for page in range(3):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(1)
    liList = driver.find_elements_by_xpath('//ul[@class="gl-warp clearfix"]/li')
    for li in liList:
        price = li.find_element_by_tag_name("i").text
        info = li.find_element_by_xpath(".//div[@class='p-name p-name-type-2']/a/em").text
        comment = li.find_element_by_xpath(".//div[@class='p-commit']/strong/a").text
        try:
            shop = li.find_element_by_xpath(".//div[@class='p-shop']/span/a").get_attribute("title")
        except:
            shop = "无"
        print(info,price,comment,shop)

    sleep(random.Random().randrange(1, 20) / 10)
    driver.find_element_by_xpath("//a[@class='pn-next'][contains(.,'下一页>')]").click()