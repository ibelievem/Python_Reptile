# 浏览器驱动
from selenium import webdriver
import time

# 声明一个驱动对象
driver = webdriver.Firefox()

# 请求页面
driver.get("http://www.baidu.com")

# 获得页面源代码
print(driver.page_source)

# 获得当前链接
print(driver.current_url)

# 获取cookies
print(driver.get_cookies())

# 标题
print(driver.title)

# 找到元素 进行输入
driver.find_element_by_xpath("//input[@id='kw']").send_keys("996")
time.sleep(3)

# 找到元素 模拟点击
driver.find_element_by_xpath("//input[@id='su']").click()
time.sleep(3)

driver.save_screenshot("./截图.png")

# 后退
driver.back()
time.sleep(3)

# 前进
driver.forward()
time.sleep(3)

# 关闭
driver.close()