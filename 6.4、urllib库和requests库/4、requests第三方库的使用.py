#urllib的封装
import requests

url="http://www.baidu.com"


#get==>urllib中的 request.urlopen()
response=requests.get(url)


#打印结果为：<Response [200]> <class 'requests.models.Response'>
print(response,type(response))


#获取字节数据, read()
htmlBytes=response.content

#解码
print(htmlBytes.decode())
