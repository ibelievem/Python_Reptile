import requests
from lxml import etree
from fake_useragent import UserAgent
import chardet
import lxml
import os

url = "https://www.qiushibaike.com/8hr/page/1/"
userAgent = UserAgent()
ua = userAgent.random
print(ua)
headers = {
    "User-Agent" : ua
}
response = requests.get(url,headers=headers)
html = response.text
dom = etree.HTML(html)
nodeList = dom.xpath("//div[@class='recommend-article']/ul/li")
print(len(nodeList))
index = 0
for node in nodeList:
    index = index + 1
    className = node.xpath("./@class")[0]
    if(className != "item"):
        userName = node.xpath(".//span[@class='recmd-name']/text()")[0]
        userIcon = node.xpath(".//a[@class='recmd-user']/img/@src")[0]
        userIcon = "https:" + userIcon
        title = node.xpath(".//div[@class='recmd-right']/a/text()")
        recmdNum = node.xpath(".//div[@class='recmd-num']/span")
        length = len(recmdNum)
        if(length == 0):
            likeNum = 0
            commentNum = 0
        if(length == 2):
            likeNum = recmdNum[0].xpath("./text()")[0]
            commentNum = 0
        if(length == 5):
            likeNum = recmdNum[0].xpath("./text()")[0]
            commentNum = recmdNum[3].xpath("./text()")[0]
        print("用户名",userName,"图标",userIcon,"点赞数",likeNum,"评论数",commentNum,"标题",title)

    #     if(not os.path.exists("./" + str(index))):
    #         os.makedirs("./" + str(index))
    #
    #     href = node.xpath("./a/@href")[0]
    #     url = "https://www.qiushibaike.com" + href
    #     childHtml = requests.get(url,headers=headers)
    #     childDom = etree.HTML(childHtml.text)
    #     if (className == "item typs_video"):
    #         print("视频贴")
    #         url = childDom.xpath("//video[@id='article-video']/source/@src")[0]
    #         url = "https:" + url
    #         vedieContent = requests.get(url,headers=headers).content
    #         with open("./" + str(index) + "/" + userName + ".mp4","wb") as f:
    #             f.write(vedieContent)
    #     if (className == "item typs_multi"):
    #         print("多图贴")
    #         imgList = childDom.xpath("//div[@class='thumb']/img/@src")
    #         imgIndex = 0
    #         for img in imgList:
    #             imgIndex = imgIndex + 1
    #             img = "http:" + img
    #             imgContent = requests.get(img, headers=headers).content
    #             if(img.find("gif") != -1):
    #                 fileName = "./"  + str(index) + "/" + userName + str(imgIndex) + ".gif"
    #             else:
    #                 fileName = "./"  + str(index) + "/" + userName + str(imgIndex) + ".jpg"
    #             with open(fileName, "wb") as f:
    #                 f.write(imgContent)
    #     if (className == "item typs_word"):
    #         print("文字贴")
    #     if (className == "item typs_image"):
    #         print("单图贴")
    # if(className == "item"):
    #     print("广告贴")