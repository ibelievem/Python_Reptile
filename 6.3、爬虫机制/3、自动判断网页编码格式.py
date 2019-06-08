# chardet 第三方库
# 用来判断编码的模块
# 使用chardet.detect()方法，判断网页的编码格式
# 安装方法： pip install chardet

#urllib 内置请求库，request 请求模块
from urllib import request
import chardet

url="http://www.baidu.com"

#请求一个url地址
response=request.urlopen(url)
print(type(response))

#读取网页信息，返回bytes信息
result=response.read()

#编码判断
detectResult=chardet.detect(result)
print(detectResult,type(detectResult))

#获取网页的编码：detectResult["encoding"]
#把 bytes 通过 相对应的编码格式 转换为 str
html=result.decode(detectResult["encoding"])
print(html)












