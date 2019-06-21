import requests
import re


headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
}
html = requests.get("https://www.baidu.com",headers=headers).content.decode()
# print(html)

# print("====================================")

# 匹配title标签之间的文本值 title没有任何其他属性干扰
# pattern = re.compile("<title>(.*?)</title>")
# print(pattern.findall(html))

# 相当于 xpath中 //a/text() 取所有a标签的文本值
# pattern = re.compile("<a.*?>(.*?)</a>",re.M|re.S)
# aTagList=pattern.findall(html)
# print(len(aTagList))
# for aTag in aTagList:
#     print(aTag)


# 抓取所有a标签且a标签class为mnav的文本值  //a[@class="mnav"]/text()
# pattern = re.compile('<a.*?class="mnav">(.*?)</a>',re.M|re.S)
# aTagList=pattern.findall(html)
# print(len(aTagList))
# for aTag in aTagList:
#     print(aTag)


# 抓取所有a标签且a标签class为mnav的href属性  相当于xpath中的 //a[@class="mnav"]/@href
# pattern = re.compile('<a href="(.*?)".*?class="mnav".*?</a>',re.M|re.S)
# aTagList=pattern.findall(html)
# print(len(aTagList))
# for aTag in aTagList:
#     print(aTag)



# # 先做一次筛选 缩小范围
pattern = re.compile('<div id="u1">(.*?)</div>',re.M|re.S)
html = pattern.findall(html)[0]
# print(html)

print(len(html))
pattern = re.compile('<a.*?href="(.*?)".*?class="mnav".*?>.*?</a>',re.M|re.S)
aTagList = pattern.findall(html)

print(len(aTagList))
for aTag in aTagList:
    print(aTag)


