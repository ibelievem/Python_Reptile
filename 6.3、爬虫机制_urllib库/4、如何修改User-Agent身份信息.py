from urllib import request

url="http://www.useragentstring.com/"


#构造字典，修改请求头信息
headers={
    "User-Agent":"Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)",
}

#通过urllib的 Request对象 替换身份信息
req=request.Request(url,headers=headers)


htmlBytes=request.urlopen(req).read()
#解码输出
print(htmlBytes.decode())
