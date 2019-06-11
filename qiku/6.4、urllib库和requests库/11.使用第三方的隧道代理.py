import requests

#1
# 蘑菇代理的隧道订单
appKey = "UEtNWWRaekRndDFLNUc0UDpsMmd2c2J5SHZNZVRncHdp"

# 蘑菇隧道代理服务器地址
ip_port = 'transfer.mogumiao.com:9001'

#2
# 准备去爬的 URL 链接
url = 'http://ip.27399.com/'

proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port}
headers = {"Proxy-Authorization": 'Basic '+ appKey}
r = requests.get(url, headers=headers, proxies=proxy,verify=False,allow_redirects=False)
print(r.status_code)
#3 修改显示
print(r.content.decode())
if r.status_code == 302 or r.status_code == 301 :
    loc = r.headers['Location']
    url_f = url + loc
    print(loc)
    r = requests.get(url_f, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
    print(r.status_code)
    print(r.content.decode())