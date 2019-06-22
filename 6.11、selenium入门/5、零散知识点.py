from selenium import webdriver
from time import sleep

# # 执行js脚本
# driver = webdriver.Firefox()
# driver.get("https://www.jd.com/")
# sleep(2)
# # # 窗口滑动到底部
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
# sleep(2)
#
# driver.quit()


#用于后期图片剪裁的一些属性
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
logoImg=driver.find_element_by_xpath("//area[@title='点击一下，了解更多']")
driver.save_screenshot("logi.png")

print(logoImg.id)
print(logoImg.tag_name)


# 如果这两个属性截图，保持电脑分辨率为1920*1080  缩放为100%
# 操作的时候尽量使用 .maximize_window
print(logoImg.location)
print(logoImg.size)


