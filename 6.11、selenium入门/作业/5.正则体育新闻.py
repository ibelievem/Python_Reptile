import re
import requests
import fake_useragent

ua = fake_useragent.UserAgent().random
print(ua)
headers = {
    "User-Agent" : ua
}
html = requests.get("http://sports.163.com/zc/",headers = headers).text


newsList = re.findall('<div class="news_item">.*?<div class="share">',html,re.S)

index = 1
for news in newsList:
    titleAndUrl = re.findall('<h3>(.*?)</h3>',news,re.S)
    url = re.findall('href="(.*?)"',titleAndUrl[0])[0]
    title = re.findall('">(.*?)</a>',titleAndUrl[0])[0]
    keywords = re.findall('<div class="keywords">(.*?)</div>',news,re.S)
    keywords = re.findall('">(.*?)</a>', keywords[0])[0]
    comment = re.findall('<span class="icon">(.*?)</span>',news,re.S)[0]
    print(url,"    ",title,"    ",keywords,"    ",comment)