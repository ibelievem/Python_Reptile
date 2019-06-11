import requests

#加入浏览器的标识
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
}


#1、通过参数 params 拼接 url
# params={
#     "wd":"计算机"
# }
#
# url_temp="http://www.baidu.com/s?"
#
##将params和url拼接在一起
# r=requests.get(url_temp,headers=headers,params=params)
# print(r.status_code)
# print(r.request.url)



#2、手动拼接url
url="http://www.baidu.com/s?wd={}".format("计算机")
r=requests.get(url,headers=headers)
print(r.status_code)
print(r.request.url)