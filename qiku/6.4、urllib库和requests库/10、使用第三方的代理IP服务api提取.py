import requests

response = requests.get("http://piping.mogumiao.com/proxy/api/get_ip_bs?appKey=c913f23ce5384bfcb1d3c260d36a6a23&count=4&expiryDate=0&format=1&newLine=2")

#拿到的是json字符串，把字符串转化为python对象：dict、list
ipInfo = response.json()
ipList = ipInfo["msg"]
for item in ipList:
    ip = item["ip"]+":"+item["port"]
    print(ip)

