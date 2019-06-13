# chrome headless
# firefox headless

from selenium import webdriver

# 火狐浏览器配置选项对象
chromeOptions = webdriver.ChromeOptions()
chromeOptions.set_headless()

driver = webdriver.Chrome(chrome_options=chromeOptions)
driver.get("http://www.baidu.com")
print(driver.page_source)
driver.save_screenshot("./谷歌无头截图.png")