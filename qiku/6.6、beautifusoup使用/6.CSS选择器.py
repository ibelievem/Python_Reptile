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

#root.xpath(表达式) //标签名
# result = soup.select("a")
# //标签名/@属性名
# print(item["href"])

# //*[@class="属性值"]
# result = soup.select(".sister")
# //*[@id="属性值"]
# result = soup.select("#link1")
# //head/title
# result = soup.select("head > title")
# //body//*[@id="link1"]
# result = soup.select("body #link1")
# //p[@id="link1"]   'img[class=""]["bpic"]'
# result = soup.select('p[id="link1"]')
# //body//a[@href="http://example.com/elsie"]
result = soup.select('body a[href="http://example.com/elsie"]')

print(len(result))
for item in result:
    print(item)

