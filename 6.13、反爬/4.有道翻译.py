# salt
# r = '' + (new Date).getTime(),
# i = r + parseInt(10 * Math.random(), 10);
# sign
# 'fanyideskweb' + e + i + '@6f#X3=cCuncYssPsuRUE'
# ts  salt[:-1]
# bv e2a78ed30c66e16a857c5b6486a1d326

import execjs
import hashlib
import requests


# 通过执行js拿到一个参数
jsCode = execjs.compile("""
    function GetSalt(){
        r = '' + (new Date).getTime();
        i = r + parseInt(10 * Math.random(), 10);
        return i;
    };
""")
salt = jsCode.call("GetSalt")

md5 = hashlib.md5()
parames = 'fanyideskweb' + "world" + str(salt) + '@6f#X3=cCuncYssPsuRUE'
# 传参
md5.update(parames.encode())
# 取出散列结果
sign = md5.hexdigest()

bv = "e2a78ed30c66e16a857c5b6486a1d326"
ts = salt[:-1]


# 有道翻译url
url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
# post的参数
parameter = {
    "i":"world",
    "from":"AUTO",
    "to":"AUTO",
    "smartresult":"dict",
    "client":"fanyideskweb",
    "salt":salt,
    "sign":sign,
    "ts":ts,
    "bv":"e2a78ed30c66e16a857c5b6486a1d326",
    "doctype":"json",
    "version":"2.1",
    "keyfrom":"fanyi.web",
    "action":"FY_BY_REALTlME",
}

headers = {
    "Host":"fanyi.youdao.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding":"gzip, deflate",
    "Referer":"http://fanyi.youdao.com/",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With":"XMLHttpRequest",
    "Content-Length":"242",
    "Connection":"keep-alive",
}

cookie = {
    "___rl__test__cookies":"1560414115083",
    "_ntes_nnid":"198b03f24c29a06facf7129053d5211b,1538992682919",
    "JSESSIONID":"aaacHxe3S6fHm-dOz1pTw",
    "OUTFOX_SEARCH_USER_ID":"-1473797891@106.2.43.13",
    "OUTFOX_SEARCH_USER_ID_NCOO":"1993276325.6636539",
    "YOUDAO_MOBILE_ACCESS_TYPE":"1",
}

# 拿到的是json字符串，把字符串转化为python对象 dict,list
pythonObj = requests.post(url,data=parameter,headers=headers,cookies=cookie).json()

print(pythonObj)
print(type(pythonObj))
# 按索引取结果
print(pythonObj["translateResult"][0][0]["tgt"])
