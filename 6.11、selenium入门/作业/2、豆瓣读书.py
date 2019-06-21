import requests
from lxml import etree

url="https://book.douban.com/latest"

response=requests.get(url)

html=response.content.decode()

# 把html格式的字符串 转化为一个树形结构
root=etree.HTML(html)

# 根据 路径表达式 取出需要的节点和数据
result=root.xpath("//div[@class='grid-12-12 clearfix']//li")

for i in result:
    title=i.xpath("./div/h2/a/text()")[0]
    score=i.xpath(".//span[2]/text()")[0].replace(" ","").replace("\n","")
    publish=i.xpath(".//p[2]/text()")[0].replace(" ","").replace("\n","")
    introduce=i.xpath(".//p[3]/text()")[0].replace(" ","").replace("\n","")
    print("书名：%s\t评分：%s\t出版信息：%s\t简介：%s"%(title,score,publish,introduce))


