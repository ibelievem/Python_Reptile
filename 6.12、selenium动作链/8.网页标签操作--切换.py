from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

# 打开百度
driver.get("http://www.baidu.com")
sleep(3)
# 当前浏览器的标签集合
print(len(driver.window_handles))
print(driver.window_handles)
print("=============================================")
sleep(2)

# 打开拼多多
# # 新建标签页
driver.execute_script("window.open()")
# # 切换标签页
driver.switch_to_window(driver.window_handles[1])
driver.get("http://www.pinduoduo.com")
print(len(driver.window_handles))
print(driver.window_handles)
print("=============================================")
sleep(2)


# 打开淘宝
# # 新建标签页
driver.execute_script("window.open()")
# # 切换标签页
driver.switch_to_window(driver.window_handles[2])
driver.get("http://www.taobao.com")
sleep(2)

# 切换到拼多多
driver.switch_to_window(driver.window_handles[1])
sleep(2)

# 切换到百度
driver.switch_to_window(driver.window_handles[0])
sleep(2)

# 关闭浏览器
# 方法1
driver.quit()
# 方法2
# driver.close()