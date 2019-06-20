# switch_to_alert    切换到弹窗
# accept                 点击【确认】按钮
# dismiss                点击【取消】按钮（如有按钮）
# send_keys            输入内容（如有输入框）

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.alert import Alert

driver = webdriver.Firefox()
driver.get("http://sahitest.com/demo/alertTest.htm")
sleep(3)

clickForAlert = driver.find_element_by_xpath("//input[@name='b1']")
clickForAlert.click()
sleep(3)
# 切换到弹窗对象
alert = driver.switch_to_alert()
print(alert)
# class 'selenium.webdriver.common.alert.Alert'
print(type(alert))
# 点击确定按钮
alert.accept()

