import requests

response=requests.get("http://www.baidu.com")

#请求的url地址
print(response.request.url)

#响应的url地址
print(response.url)

#请求的头
print(response.request.headers)

#打印访问的内容
print(response.content.decode())

