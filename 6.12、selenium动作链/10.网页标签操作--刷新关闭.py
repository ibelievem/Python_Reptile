from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

# 打开百度
driver.get("http://www.baidu.com")


# 新建标签页，打开拼多多
driver.execute_script("window.open()")
# 切换标签页
driver.switch_to_window(driver.window_handles[1])
driver.get("http://www.pinduoduo.com")


# 新建标签页，打开淘宝
driver.execute_script("window.open()")
driver.switch_to_window(driver.window_handles[2])
driver.get("http://www.taobao.com")


# F5 刷新
for i in range(3):
    sleep(2)
    driver.refresh()

# 关闭当前标签页
# driver.close()
# sleep(2)

# 切换到该窗口并关闭
# driver.switch_to_window(driver.window_handles[1])
# driver.close()
# sleep(2)

# 切换到该窗口并关闭
# driver.switch_to_window(driver.window_handles[0])
# driver.close()

# 关闭浏览器
# driver.quit()
