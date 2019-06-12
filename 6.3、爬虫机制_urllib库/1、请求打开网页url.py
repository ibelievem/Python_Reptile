#1、模块导入
from urllib import request

#2、定义url
url="http://www.baidu.com"

#3、请求一个url地址，返回一个对象的类型
response=request.urlopen(url)
print(type(response)) ##<class 'http.client,HTTPResponse'> 服务器应答的数据包含在这个类里

#4、读取并打印网页的信息
result=response.read()
print(result)
print(type(result))

#5、将bytes转化为str(解码)
html=result.decode()
print(html,type(html))



