from bs4 import BeautifulSoup
from bs4.element import NavigableString

html_doc = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="title" id="link1">p标签的内容<b>The Dormouse's story</b></p>

        <p class="story">Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
            <a href="http://example.com/lacie" class="sister" id="link1">Lacie</a> and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.
        </p>

        <p class="story">...</p>
"""

# 构造树形结构 etree.HTML()
soup = BeautifulSoup(html_doc,"lxml")

# Tag类型的相关操作
# # 输出类型
# # print(soup)
# print(type(soup))
#
# # 根节点.标签名 访问第一个符合的标签
# titleTag = soup.title
# print(titleTag)
# print(type(titleTag))
#
# aTag = soup.a
# print(aTag)
# print(type(aTag))
#
# # 属性列表
# print(soup.a.attrs)
# # 访问属性
# print(soup.a["class"])
# # 访问属性
# print(soup.a.get("class"))
#
# # 属性可读可写
# print(soup.p["class"])
# soup.p["class"] = "newClass"
# print(soup.p["class"])
#
# # 支持删除操作
# del soup.p["class"]
# print(soup.p)

# string 获取第一个p标签的内部值
# print("p标签的内容")
# innerHtml = soup.p.string
# print(innerHtml)
# print(type(innerHtml))
#
# print("b标签的内容")
# innerHtml = soup.b.string
# print(innerHtml)
# print(type(innerHtml))

# 根对象 等同于Tag
# print(soup.name)
# print(type(soup))
# print(soup.attrs)

# bs4.element.Comment
# aStr = soup.a.string
# print(aStr)
# print(type(aStr))

# .children .content == /*
# 访问某一标签所有的子集标签
# tagList = soup.body.children
# print(type(tagList))
# print(tagList)
# for tag in tagList:
#     print(tag)

# descendants == //*
# tagList = soup.body.descendants
# print(type(tagList))
# print(tagList)
# for tag in tagList:
#     print(tag)






