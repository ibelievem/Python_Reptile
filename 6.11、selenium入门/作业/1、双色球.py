import requests
from lxml import etree


url="http://zst.aicai.com/ssq/openInfo/"

# 请求url地址,返回 <Response [200]>
response=requests.get(url)

# 将请求的网页解码为utf-8
html=response.content.decode()

# 把html格式的字符串 转化为一个树形结构
root=etree.HTML(html)

result=root.xpath("//tbody/tr[@onmouseout]")

for i in result:
    res = i.xpath("./td/text()")
    print(res)




