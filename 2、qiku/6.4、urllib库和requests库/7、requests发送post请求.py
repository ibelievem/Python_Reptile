import requests

#有道翻译url
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

# post的参数
parameter = {
    "i":"alice",
    "from":"AUTO",
    "to":"AUTO",
    "smartresult":"dict",
    "client":"fanyideskweb",
    "salt":"15577378774445",
    "sign":"44163461e046a197ba4681e91aa49524",
    "ts":"1557737877444",
    "bv":"e2a78ed30c66e16a857c5b6486a1d326",
    "doctype":"json",
    "version":"2.1",
    "keyfrom":"fanyi.web",
    "action":"FY_BY_REALTlME",
}


#拿到的是json字符串，把字符串转化为python对象：dict、list
pythonObj=requests.post(url,data=parameter).json()



print(pythonObj,type(pythonObj))


#按照索引取结果
print(pythonObj["translateResult"][0][0]["tgt"])