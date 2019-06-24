from selenium import webdriver
from time import sleep
# expected_conditions 类，负责条件触发
from selenium.webdriver.support import expected_conditions as EC
# WebDriverWait 库，负责循环等待
from selenium.webdriver.support.ui import WebDriverWait
# 查找方式的库
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.taobao.com/")

try:
    # 循环等待对象
    webDriverWait = WebDriverWait(driver,5)
    # 判断元素是否加载成功
    webDriverWait.until(EC.presence_of_element_located((By.XPATH,'//a[@class="logo-bd clearfix"]')))
except Exception as e:
    print(e)
    with open("./log.txt","w") as f:
        f.write(e)
    driver.quit()
print("加载成功")
print(driver.find_element_by_tag_name("title"))
driver.quit()


