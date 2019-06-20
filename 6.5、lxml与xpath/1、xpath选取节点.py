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
# print(root,type(root))

#把对象 字符串化
# print(etree.tostring(root).decode())


# 根据 路径表达式 取出需要的节点和数据

# 1、/ 按照写死的路径 找到所有符合的标签
# result = root.xpath("/bookstore/coffee/price")


# 2、// 按标签取标签 不管位置
# result = root.xpath("//book/price")


# 3、. 是当前标签
# result = root.xpath("./book/.")


# 4、爬虫数据-json数据处理、.. 是当前标签的上一级
# result = root.xpath("./book/..")


# 5、@ 获取标签内的属性值
result = root.xpath("//book/@id")


# 6、text() 取标签元素的内容
# result = root.xpath("//book/name/text()")


# 遍历对象列表
for tag in result:
    try:
        # 把对象 字符串化，显示对象的内容
        print(etree.tostring(tag).decode())
    except:
        print(tag)
