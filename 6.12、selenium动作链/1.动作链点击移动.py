from selenium import webdriver
import time
# 比较长 导入动作链类
from selenium.webdriver.common.action_chains import ActionChains

url='http://sahitest.com/demo/clicks.htm'

driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)

# 找到需要操作的元素
dbclickElement = driver.find_element_by_xpath("//input[@value='click me']")
rightclickElement = driver.find_element_by_xpath("//input[contains(@value,'dbl click me')]")
leftclickElement = driver.find_element_by_xpath("//input[contains(@value,'right click me')]")

# 如果只需要左键点击某一个元素 不需要是使用动作链
# leftclickElement.click()


# 两种写法
# 1、构造一个动作链对象 链式写法是连续执行的
# ActionChains(driver).double_click(dbclickElement).click(leftclickElement).context_click(rightclickElement).perform()

# 2、分部写法 如果需要操作之间有时间停顿 分部写每一步都是一个新的动作链对象 避免动作重复
# actionChains = ActionChains(driver)
# # 左键双击
# actionChains.double_click(dbclickElement)
# actionChains.perform()
# time.sleep(2)

# actionChains = ActionChains(driver)
# # 左键单击
# actionChains.click(leftclickElement)
# actionChains.perform()
# time.sleep(2)
#
# actionChains = ActionChains(driver)
# # 右键单击
# actionChains.context_click(rightclickElement)
# actionChains.perform()


time.sleep(1)
driver.close()
