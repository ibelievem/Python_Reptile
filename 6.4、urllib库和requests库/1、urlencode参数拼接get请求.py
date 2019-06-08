from urllib import parse,request

url="http://www.baidu.com/s?"

paramDic={
    "wd":"端午节"
}

#将字典转化为url需要的参数格式(字典的冒号变为等号)
subUrl=parse.urlencode(paramDic)

#地址+参数
url=url+subUrl


#请求一个url地址，返回一个对象的类型
response=request.urlopen(url)

#读取并打印网页的信息
result=response.read()

#将bytes转化为str(解码)
html=result.decode()
print(html,type(html))



