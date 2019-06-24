from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("http://sahitest.com/demo/mouseover.htm")
sleep(1)

# 找到需要鼠标移动指向的元素
hiElement = driver.find_element_by_xpath("//span[contains(.,'Hi Kamlesh')]")
writeElement = driver.find_element_by_xpath("//input[@value='Write on hover']")
blankElement = driver.find_element_by_xpath("//input[@value='Blank on hover']")


# 主要用这种，直接确定到某一个元素
actionChains = ActionChains(driver)
# 鼠标移动到某一个元素
actionChains.move_to_element(hiElement).perform()
sleep(1)


# 偏移确定该元素，不常用
# actionChains = ActionChains(driver)
# # 鼠标在当前位置进行偏移
# actionChains.move_by_offset(10,25).perform()
# sleep(1)


# 偏移确定该元素，不常用
# actionChains = ActionChains(driver)
# # 鼠标在当前位置进行偏移
# actionChains.move_to_element_with_offset(writeElement,5,55)
# sleep(2)


driver.close()