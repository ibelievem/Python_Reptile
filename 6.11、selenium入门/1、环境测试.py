# 导入selenium的web驱动对象
from selenium import webdriver
from time import sleep

# 选择创建一个浏览器驱动对象
driver = webdriver.PhantomJS(executable_path=r"E:\phantomjs-2.1.1-windows\bin\phantomjs.exe")
#浏览器驱动对象打开一个网页
driver.get("http://www.baidu.com")
# 打印当前浏览器驱动加载的页面源码
print(driver.page_source)

sleep(1)
print("====================================")

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
print(driver.page_source)

sleep(1)
print("====================================")

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
print(driver.page_source)

sleep(1)
print("====================================")
