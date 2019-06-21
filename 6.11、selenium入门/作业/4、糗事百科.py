import requests
from lxml import etree

url="https://www.qiushibaike.com/8hr/page/2/"

response=requests.get(url)

html=response.content.decode()

root=etree.HTML(html)


result=root.xpath("//div[@class='recommend-article']/ul/li")

for i in result:
    title=i.xpath(".//a[@class='recmd-content']/text()")[0]
    num=i.xpath(".//div[@class='recmd-num']/span[1]/text()")[0]+i.xpath(".//div[@class='recmd-num']/span[2]/text()")[0]
    comment=i.xpath(".//div[@class='recmd-num']/span[4]/text()")[0]+i.xpath(".//div[@class='recmd-num']/span[5]/text()")[0]
    author = i.xpath(".//span[@class='recmd-name']/text()")[0]
    print(title,num,comment,author)





