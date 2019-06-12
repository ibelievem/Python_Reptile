#urllib的封装
import requests

url="http://www.baidu.com/s"

headers={
    "User-Agent":"Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)",
}

params={
    'wd':'笔记本'
}

#get==>urllib中的 request.urlopen()
response=requests.get(url,params=params,headers=headers)


#打印结果为：<Response [200]> <class 'requests.models.Response'>
print(response,type(response))


#获取字节数据, read()
htmlBytes=response.content

#解码
print(htmlBytes.decode())
