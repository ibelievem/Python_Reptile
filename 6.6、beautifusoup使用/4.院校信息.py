import requests
from lxml import etree
import time
from proxyTool import ProxyTool

schoolHomeUrlDic = {}

for i in range(1):
    time.sleep(2)
    # 请求所有学校信息
    url = "https://gaokao.chsi.com.cn/sch/search.do?searchType=1&ssdm=41&start={0}".format(i * 20)
    # 代理请求简单封装了一下
    htmlStr = ProxyTool.GetHtml(url)
    root = etree.HTML(htmlStr)
    # 取学校名和主页链接
    domain = "https://gaokao.chsi.com.cn"
    hrefList = root.xpath('//td[@class="js-yxk-yxmc"]/a/@href')
    schoolNameList = root.xpath('//td[@class="js-yxk-yxmc"]/a/text()')
    # 记录第一级界面的信息 数据存到一个字典里 key = 学校名 value= 主页链接
    for i in range(len(hrefList)):
        name = schoolNameList[i].replace(" ","").replace("\r","")
        href = domain + hrefList[i]
        schoolHomeUrlDic[name] = href
    print(schoolHomeUrlDic)

for schoolName in schoolHomeUrlDic.keys():
    time.sleep(2)
    # 学校对应的主页链接
    majorHref = schoolHomeUrlDic[schoolName]
    print(schoolName,majorHref)
    #  第二级界面 找到专业介绍对应的url
    root = etree.HTML(ProxyTool.GetHtml(majorHref))
    nextPageUrl = root.xpath("//a[contains(.,'专业介绍')]/@href")[0]
    #  第三级界面 专业类别 专业名字信息
    root = etree.HTML(ProxyTool.GetHtml(domain + nextPageUrl))
    typeList = root.xpath('//div[@class="container"]/div[2]//div[contains(@class,"tab-item js-tab")]/a/text()')
    majorList = root.xpath('//div[@class="container"]/div[2]//div[contains(@class,"item-content js-current-item")]')
    for i in range(len(typeList)):
        datas = majorList[i].xpath('.//li/a/text()')
        for item in datas:
            print(schoolName,typeList[i],item)
    print("===============================================")


