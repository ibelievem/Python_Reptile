from urllib import parse,request,error
import json

#有道翻译url
url = "https://movie.douban.com/j/chart/top_list?"

# get 参数
parameter = {
    'type':'24',
    'interval_id':'100:90',
    'action':'unwatchedv',
    'start':'0',
    'limit':'20',
}


#get的参数直接拼接到url
url=url+parse.urlencode(parameter)
print(url)


##捕捉异常
try:
    #data参数为空，是get请求
    res=request.urlopen(url).read().decode()
    print(res)
    print(type(res))
except error.URLError as e:
    if (hasattr(e,'code')):
        print("http error"+str(e.code))

    if (hasattr(e,'reason')):
        print("url error"+str(e.reason))


# # class 'str'>,得到的是字符串类型
# print(res)
# print(type(res))
#
#
# #拿到的是json字符串，把字符串转化为python对象：dict、list
# pythonObj=json.loads(res)
# print(pythonObj)
# print(type(pythonObj))
#
# for data in pythonObj:
#     print(data)
#     print(data['title'])
