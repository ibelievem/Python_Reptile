from selenium import webdriver
import time

url = "http://www.weibo.com/login.php"
driver = webdriver.Firefox()
driver.get(url)
driver.implicitly_wait(10)

userName = driver.find_element_by_xpath("//input[@id='loginname']")
password = driver.find_element_by_xpath("//input[@type='password']")
login = driver.find_element_by_xpath("//div[@class='info_list login_btn']/a")

userName.send_keys("18668120679")
time.sleep(1)
password.send_keys("ksws0231401")
time.sleep(2)
login.click()

driver.get("https://weibo.com/p/1003061826792401?is_hot=1")
itemList = driver.find_elements_by_xpath('//div[@class="WB_cardwrap WB_feed_type S_bg2 WB_feed_like "]')
for item in itemList:
    print(item.find_element_by_xpath('.//div[@class="WB_detail"]/div[@class="WB_text W_f14"]').text)
    infoList = item.find_elements_by_xpath('.//div[@class="WB_handle"]//li[position()>1]')
    for info in infoList:
        tag = info.find_element_by_xpath('.//span[@class="line S_line1"]//em[2]')
        print(tag.text)



# 访问前添加所有cookie的键值对通过driver.add_cookie方法
# name value 为cookie的键值对  后边信息一致就可以了
# driver.add_cookie({'name': 'login_sid_t', 'value': 'd715789734d550425072e2f901892475', 'path': '/', 'domain': '.[图片]weibo.com', 'secure': False, 'httpOnly': False})
# #...
# #...
# driver.get("url")