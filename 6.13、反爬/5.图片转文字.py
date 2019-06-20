#
from PIL import Image
import pytesseract

# 打开图片
img = Image.open("./test1.PNG")
# 图片转字符串
res = pytesseract.image_to_string(img)
print(res)

# # 打开图片
# img = Image.open("./test.PNG")
# # 图片转字符串
# res = pytesseract.image_to_string(img)
# print(res)




