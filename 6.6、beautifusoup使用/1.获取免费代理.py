import requests
from lxml import etree
from fake_useragent import FakeUserAgent
import time

for i in range(1,6,1):
   print("页数:" + str(i))
   url = "https://www.kuaidaili.com/free/inha/{0}/".format(i)
   fakeUserAgent = FakeUserAgent()
   ua= fakeUserAgent.random
   headers = {
      "User-Agent":ua
   }
   response = requests.get(url,headers=headers)
   htmlStr = response.content.decode()
   root = etree.HTML(htmlStr)
   # 每一行数据的元素标签
   trList = root.xpath("//tbody//tr")
   # print("根节点信息")
   # print(root)
   # print(type(root))
   for tr in trList:
      # print("tr节点信息")
      # print(tr)
      # print(type(tr))
      # // tbody // tr[索引]/td[4]/text()[0]
      type = tr.xpath("./td[4]/text()")[0]
      ip = tr.xpath("./td[1]/text()")[0]
      port = tr.xpath("./td[2]/text()")[0]
      proxy = ip + ":" + port
      print(type,proxy)
   time.sleep(2)





