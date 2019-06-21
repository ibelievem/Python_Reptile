import requests
from lxml import etree
import re

html = requests.get("http://tieba.baidu.com/f/search/res?qw=%E6%99%AF%E5%90%A7&sm=2&cf=1&ie=utf-8&red_tag=k3287472406").content.decode("gbk")
# print("原始请求信息")
# print(html)
# print(len(html))
# print("===============================================")
# print("lxml处理过后的信息")
root = etree.HTML(html)
# print(etree.tostring(root).decode())
# print(len(etree.tostring(root)))
# print("===============================================")
# contentList = root.xpath('//div[@class="p_content"]')
# print("使用xpath技术 目标结果长度")
# 使用 xpath 取不到数据
# print(len(contentList))
# print(contentList)

# print("使用re技术 目标结果长度")
contentList = re.findall('<div class="p_content".*?>(.*?)</div>',html)
print(len(contentList))
for i in contentList:
    print(i)

