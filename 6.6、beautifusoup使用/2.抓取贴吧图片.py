import requests
from lxml import etree
import time
import os

def DownLoad(start,end,name):
    index = 0
    print(start,end,name)
    os.mkdir("image")
    for i in range((start-1)*50,(end-1)*50+1,50):
        index = index + 1
        #构造参数
        params = {
            "kw":name,
            "ie":"utf-8",
            "pn":i,
        }
        url = "https://tieba.baidu.com/f?"
        html = requests.get(url,params=params).content.decode()
        dom = etree.HTML(html)
        urlList = dom.xpath("//img[@class='threadlist_pic j_m_pic ']/@bpic")
        index = 0
        for url in urlList:
            print(url)
            index = index + 1
            with open("./image/" + name + str(index) + ".jpg", "wb") as pic:
                pic.write(requests.get(url).content)
        time.sleep(2)

DownLoad(1,2,"手机")


