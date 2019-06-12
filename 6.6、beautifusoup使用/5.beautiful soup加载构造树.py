from bs4 import BeautifulSoup
from bs4.element import NavigableString

html_doc = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="title" id="link1"><b>The Dormouse's story</b></p>

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
# print(soup)
# print(type(soup))

###### 一、Tag（标签）
#1、获取标签
# 根节点.标签名  访问第一个符合的标签
# titleTag = soup.title
# print(titleTag)   #打印该标签的所有内容
# print(type(titleTag))
# aTag = soup.a
# print(aTag)
# print(type(aTag))


#2、获取标签属性
# print(soup.name)
# print(soup.head.name)

# # 打印a标签的所有属性为字典
# print(soup.a.attrs)


# # 访问a标签的属性为class的值
# 方式1
# print(soup.a["class"])
# 方式2
# print(soup.a.get("class"))


# # 属性可读可写,修改过属性值的类型由 列表==>变为字符串
# print(soup.p["class"])
# print(type(soup.p["class"]))
# soup.p["class"] = "newClass"
# print(soup.p["class"])
# print(type(soup.p["class"]))


# # 删除属性
# del soup.p["class"]
# print(soup.p)



###### 二、NavigableString（标签文本内容）
# 1、 .string 获取第一个p标签的内容
# innerHtml = soup.p.string
# print(innerHtml)
# print(type(innerHtml))


###### 三、BeautifulSoup（根对象） 等同于Tag
# print(soup.name)
# print(type(soup))
# print(soup.attrs)

###### 四、Comment（注释内容）
# print(soup.a.string)   #去注释
# aStr = soup.a
# print(aStr)            #带注释
# print(type(aStr))



# ===========================================
#### 遍历文档树
# .children .content == /*
# 访问某一标签所有的直接子集标签
# tagList = soup.body.children
# print(type(tagList))  #生成器类型
# print(tagList)
# for tag in tagList:
#     print(tag)


##所有子孙标签
# descendants == //*
# tagList = soup.body.descendants
# print(type(tagList))
# print(tagList)
# for tag in tagList:
#     print(tag)






