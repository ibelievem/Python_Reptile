from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
driver.maximize_window()
sleep(5)
driver.save_screenshot("./dragMe.png")

# 找到相关需要拖拽的元素
dragMe = driver.find_element_by_xpath("//div[@class='drag']")
item1 = driver.find_element_by_xpath("//div[contains(.,'Item 1')]")
item2= driver.find_element_by_xpath("//div[contains(.,'Item 2')]")
item3 = driver.find_element_by_xpath("//div[contains(.,'Item 3')]")
item4 = driver.find_element_by_xpath("//div[contains(.,'Item 4')]")

# drag_and_drop 拖某一个到某一个元素
ActionChains(driver).drag_and_drop(dragMe,item1).perform()
sleep(2)
# drag_and_drop_by_offset 按当前鼠标的位置的偏移 拖拽一个元素
ActionChains(driver).drag_and_drop_by_offset(dragMe,190,250).perform()
sleep(2)
# click_and_hold 鼠标左键持续按住一个元素 move_to_element 移动到某一个元素
# release 释放鼠标
ActionChains(driver).click_and_hold(dragMe).move_to_element(item3).release().perform()
sleep(2)
# click_and_hold 鼠标左键持续按住一个元素
# move_to_element_with_offset 移动到某一个元素再偏移一定像素
# release 释放鼠标
ActionChains(driver).click_and_hold(dragMe).move_to_element_with_offset(item3,150,10).release().perform()
sleep(2)

