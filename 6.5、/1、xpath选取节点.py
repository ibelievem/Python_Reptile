from lxml import etree

xmlStr = """
<bookstore>
    <book id="book1">
        <name type="python">学习爬虫</name>
        <price>9.9</price>
    </book>
    <book id="book2">
        <name type="pythonLib">Urllib</name>
        <price>19.9</price>
    </book>    
    <book id="book3">
        <name type="pythonLib">学习Requests</name>
        <price>999</price>
    </book>
    <coffee>
        <name type="coffee">卡布奇洛</name>
        <price>15</price>
    </coffee>
    <coffee>
        <name type="coffee">拿铁</name>
        <price>25</price>
    </coffee>
</bookstore>
"""

# 把xml格式的字符串 转化为一个树形结构
root = etree.XML(xmlStr)

# 根据路径表达式取出需要的节点和数据
# / 按照写死的路径 找到所有符合的标签
# result = root.xpath("/bookstore/coffee/price")
# // 按标签取标签 不管位置
# result = root.xpath("//book/price")
# .是当前标签
# result = root.xpath("./book/.")
# ..是当前标签的上一级
# result = root.xpath("./book/..")
# @ 取标签内的属性
# result = root.xpath("//book/@id")
# text() 取标签之间的文本之
result = root.xpath("//book/name/text()")

for tag in result:
    try:
        # 把对象 字符串化
        print(etree.tostring(tag).decode())
    except:
        print(tag)
