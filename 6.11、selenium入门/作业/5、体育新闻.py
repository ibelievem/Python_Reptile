import requests
from lxml import etree
import chardet

url="https://sports.163.com/zc/"

response=requests.get(url)

html=response.text

root=etree.HTML(html)

result=root.xpath("//div[@class='news_item']")

for i in result:
    # 取节点里面的元素值
    urls=i.xpath("./h3/a/@href")[0]
    info=i.xpath(".//div[@class='keywords']/a[1]/text()")[0]+" "+i.xpath(".//div[@class='keywords']/a[2]/text()")[0]
    times=i.xpath(".//div[@class='post_date']/text()")[0]
    print(urls,info,times)

