from selenium import webdriver
import time

url='http://www.weibo.com/login.php'

driver=webdriver.Chrome()
driver.get(url)

# 设置隐式等待
driver.implicitly_wait(2)

# # 窗口最大化
driver.maximize_window()

username=driver.find_element_by_xpath('//*[@id="loginname"]')
password=driver.find_element_by_xpath('//*[@type="password"]')
login=driver.find_element_by_xpath('//div[@class="info_list login_btn"]/a')

username.send_keys("18668120679")
time.sleep(1)
password.send_keys("ksws0231401")
time.sleep(1)
login.click()

# 关闭浏览器
driver.quit()