from selenium import webdriver
import time

url = "https://weibo.com/p/1003061826792401?is_hot=1"
driver = webdriver.Firefox()
driver.get(url)

time.sleep(10)
print(driver.page_source)

itemList = driver.find_elements_by_xpath('//div[@class="WB_cardwrap WB_feed_type S_bg2 WB_feed_like "]')
for item in itemList:
    print(item.find_element_by_xpath('.//div[@class="WB_detail"]/div[@class="WB_text W_f14"]').text)
    infoList = item.find_elements_by_xpath('.//div[@class="WB_handle"]//li[position()>1]')
    for info in infoList:
        tag = info.find_element_by_xpath('.//span[@class="line S_line1"]//em[2]')
        print(tag.text)