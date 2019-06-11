import requests
from lxml import etree
import re

headers = {
    "Host":"tb1.bdstatic.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept":"text/css,*/*;q=0.1",
    "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding":"gzip, deflate",
    "Connection":"keep-alive",
}

html = requests.get("http://tieba.baidu.com/f/search/res?qw=%E6%99%AF%E5%90%A7&sm=2&cf=1&ie=utf-8&red_tag=k3287472406").content.decode("gbk")
print("原始请求信息")
print(html)
print(len(html))
print("===============================================")
print("lxml处理过后的信息")
root = etree.HTML(html)
print(etree.tostring(root).decode())
print(len(etree.tostring(root)))
print("===============================================")
contentList = root.xpath('//div[@class="p_content"]')
print("使用xpath技术 目标结果长度")
print(len(contentList))

print("使用re技术 目标结果长度")
contentList = re.findall('<div class="p_content".*?>(.*?)</div>',html)
print(len(contentList))


