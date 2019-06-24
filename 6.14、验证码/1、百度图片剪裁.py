from selenium import webdriver
from PIL import Image
import time

url='http://www.baidu.com'

driver=webdriver.Firefox()
driver.get(url)

# 智能隐式等待5秒
driver.implicitly_wait(5)
# 窗口最大化
driver.maximize_window()

logoElement=driver.find_element_by_xpath('//area[@title="点击一下，了解更多"]')
# 相对于浏览器左上角的像素位置
print(logoElement.location)

print(logoElement.size)

driver.save_screenshot("./baidu.png")

time.sleep(2)

# 求图片矩形区域的边界
left=logoElement.location["x"]
top=logoElement.location['y']
right=left+logoElement.size["width"]
bottom=top+logoElement.size["height"]

print(left,top,right,bottom)

bd=Image.open("./baidu.png")

# 截图,根据左上右下四个边界，进行裁剪
logo=bd.crop((left,top,right,bottom))
logo.show()
logo.save("./logo.png")




