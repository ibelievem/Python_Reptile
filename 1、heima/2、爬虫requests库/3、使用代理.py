# 1、正向代理：客户端直接知道服务器的地址
# 2、反向代理：客户端不知道服务器的地址
import requests

proxies = {"http":"http://106.13.117.143:3128"}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"}

r = requests.get("http://www.baidu.com",proxies=proxies,headers=headers)

print(r.status_code)