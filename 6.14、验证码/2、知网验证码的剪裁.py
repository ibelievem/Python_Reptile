from selenium import webdriver
from PIL import Image
from time import sleep
import pytesseract

driver = webdriver.Firefox()
driver.get("http://my.cnki.net/elibregister/commonRegister.aspx#")
driver.implicitly_wait(10)
driver.maximize_window()

logoElement = driver.find_element_by_xpath('//img[@id="checkcode"]')
# 相对于浏览器左上角的像素位置
print(logoElement.location)
print(logoElement.size)
driver.save_screenshot("./bd.png")
sleep(2)
# 求图片矩形区域的边界
left = logoElement.location["x"]
top = logoElement.location["y"]
right = left + logoElement.size["width"]
bottom = top + logoElement.size["height"]

print(left,top,right,bottom)
bd = Image.open("./bd.png")
# 根据左上右下四个边界 进行剪裁
logo = bd.crop((left,top,right,bottom))
logo.save("./logo.png")


# # 打开图片转化格式 参数：图片路径   彩色图片--》0-255的灰黑白图片--》黑白图片
image = Image.open("./logo.png")
# # 有背景干扰的搞不定 做一些处理 灰度化 二值化
image.show()
# # 灰度化
gray = image.convert("L")
gray.show()
# # 二值化 if else
bw = gray.point(lambda x:0 if x < 120 else 255,'1')
bw.show()
# # 调用图片识别工具的api
res = pytesseract.image_to_string(bw)

print(res)




