from bs4 import BeautifulSoup

html_doc = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="title" id="link1">p标签的内容<b>The Dormouse's story</b></p>

        <p class="story">Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
            <a href="http://example.com/elsie" class="sister" id="link1">Lacie</a> and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.
        </p>

        <p class="story">...</p>
"""

# 构造树形结构 etree.HTML()
soup = BeautifulSoup(html_doc,"lxml")


# 1、通过标签名查找   语法格式：soup.select('标签名')
#  等同于之前的 soup.xpath(“//标签名”)
# result = soup.select("a")  # 查找所有的a标签,结果为列表类型
# print(type(result))
# print(len(result))
# for item in result:
#     print(item)
#     print(item["href"])      # 等同于 //标签名/@属性名 ，打印满足条件的属性值


# 2、通过类名查找   语法格式：soup.select('.类名')
# 等同于 //*[@class="属性值"]
# result = soup.select(".sister")
# print(len(result))
# for item in result:
#     print(item)


# 3、通过id查找   语法格式： soup.select('#id名字')
#  等同于 //*[@id="属性值"]
# result = soup.select("#link1")
# print(len(result))
# for item in result:
#     print(item)



# 4、爬虫数据-json数据处理、组合查找：直接子集查找   等同于 //head/title
# result = soup.select("head > title")
# print(type(result))
# print(len(result))
# for item in result:
#     print(item)


# 4、爬虫数据-json数据处理、组合查找：所有子孙集查找   等同于 //body//*[@id="link1"]
# 满足body下所有拥有id=link的所有子孙集
# result = soup.select("body #link1")
# print(type(result))
# print(len(result))
# for item in result:
#     print(item)


# 5、属性查找，属性和标签的双重过滤
# 等同于 //p[@id="link1"]
# result = soup.select('p[id="link1"]')
# print(len(result))
# for item in result:
#     print(item)

# 等同于 //body//a[@href="http://example.com/elsie"]
result = soup.select('body a[href="http://example.com/elsie"]')
print(len(result))
for item in result:
    print(item)





