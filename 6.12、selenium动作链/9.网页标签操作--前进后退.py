from selenium import webdriver
from time import sleep


# 单个标签的操作前进forward 后退back
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
sleep(3)

driver.find_element_by_xpath("//a[@name='tj_trnews']").click()
sleep(2)

driver.find_element_by_xpath("//a[@href='http://image.baidu.com/'][contains(.,'图片')]").click()
sleep(2)

# 标签页后退
driver.back()
sleep(2)
driver.back()
sleep(2)

# 标签页前进
driver.forward()
sleep(2)
driver.forward()
sleep(2)

driver.close()