from selenium import webdriver
from time import sleep

# # 执行js脚本
# # driver = webdriver.Firefox()
# # driver.get("https://www.jd.com/")
# # sleep(2)
# # # 窗口滑动到底部
# # driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
# # sleep(2)
# #
# # driver.quit()


#用于后期图片剪裁的一些属性
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
logoImg=driver.find_element_by_xpath("//area[@title='点击一下，了解更多']")


