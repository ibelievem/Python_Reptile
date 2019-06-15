import requests

session=requests.session()
post_url = "http://www.renren.com/PLogin.do"
post_data = {"email":"mr_mao_hacker@163.com", "password":"alarmchime"}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
}

#使用session发送post请求，cookie保存在其中
session.post(post_url,data=post_data,headers=headers)

#再使用session进行请求登陆之后才能访问的地址
r = session.get("http://www.renren.com/327550029/profile",headers=headers)

# r.content     字节类型的字节流
# r.content.decode()    解码后的字符串
# print(r.content.decode())


#保存页面
with open("renren1.html","w",encoding="utf-8") as f:
    f.write(r.content.decode())
