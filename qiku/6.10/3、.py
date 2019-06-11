import requests
import re
import time

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
}
html = requests.get("http://www.baidu.com",headers=headers).content.decode()
print(html)
# 抓取所有a标签之间的文本值
pattern = re.compile("<a .*?>(.*?)</a>",re.M|re.S)
aTagList=pattern.findall(html)
print(aTagList)

# 抓取所有a标签且a标签class为mnav的文本值  //a[@class="mnav"]/text()
pattern = re.compile('<a.*?class="mnav".*?>(.*?)</a>',re.M|re.S)
print(pattern.findall(html))
print(len(aTagList))
for aTag in aTagList:
    print(aTag)

pattern=re.compile("<a href=''")
print(time.time())






