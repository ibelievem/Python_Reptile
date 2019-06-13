import pytesseract
from PIL import Image

# 打开图片转化格式 参数：图片路径   彩色图片--》0-255的灰黑白图片--》黑白图片
image = Image.open("./test1.png")
# 有背景干扰的搞不定 做一些处理 灰度化 二值化
image.show()
# 灰度化
gray = image.convert("L")
gray.show()
# 二值化 if else
bw = gray.point(lambda x:0 if x < 10 else 255,'1')
bw.show()
# 调用图片识别工具的api
res = pytesseract.image_to_string(bw)
print(res)