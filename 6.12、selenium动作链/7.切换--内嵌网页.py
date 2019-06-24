from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://sahitest.com/demo/iframesTest.htm")
# 等待
driver.implicitly_wait(3)
print(driver.page_source)


print("===================================")


iframe = driver.find_element_by_tag_name("iframe")
# 查找到内嵌网页iframe 切换
driver.switch_to_frame(iframe)
print(driver.page_source)