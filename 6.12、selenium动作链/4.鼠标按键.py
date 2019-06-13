from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("http://sahitest.com/demo/keypress.htm")
sleep(3)

# 找到相关元素
enter = driver.find_element_by_xpath("//input[@name='t2']")
keyUp = driver.find_element_by_xpath("//label[contains(.,'Key Up')]")
keyDown = driver.find_element_by_xpath("//label[contains(.,'Key Down')]")
keyPress = driver.find_element_by_xpath("//label[contains(.,'Key Press')]")

# # 检测抬起
# ActionChains(driver).click(keyUp).click(enter).key_down("a",enter).key_up("a",enter).perform()
# sleep(2)
# # 检测按下
# ActionChains(driver).click(keyDown).click(enter).key_down("s",enter).key_up("s",enter).perform()
# sleep(2)

enter.send_keys("alsjdhfouah")
