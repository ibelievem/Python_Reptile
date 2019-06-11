import requests
from bs4 import BeautifulSoup

html = requests.get("https://book.douban.com/latest").content.decode()
root = BeautifulSoup(html,"lxml")
# //div[@class="grid-12-12 clearfix"]//li
res = root.select('div[class="grid-12-12 clearfix"] li')
print(len(res))
for li in res:
    title = li.select('h2>a')[0].string
    rate = li.select('p[class="rating"]>span')[1].string
    rate = rate.replace(" ","").replace("\n","")
    if(rate == ""):
        rate = 0
    temp = li.select('p[class="color-gray"]')[0].string.replace(" ","").replace("\n","")
    infos = temp.split("/")
    detail = li.select('p')[2].string.replace(" ","").replace("\n","")
    print(title,rate," ",infos[0]," ",infos[-2]," ",infos[-1]," ",detail)
