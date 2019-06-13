from lxml import etree

xmlStr = """
<bookstore>
    <book>
        <name type="pythonSSS">学习爬虫</name>
        <price>9.9ss</price>
    </book>
    <book id="book2">
        <name type="pythonLib">学习第三方库</name>
        <price>19.9</price>
    </book>    
    <time id="time">
        <name type="time">time</name>
        <price>time</price>
    </time>
    <coffee>
        <name type="coffeeB">卡布奇洛</name>
        <price>15</price>
    </coffee>
    <coffee>
        <name type="coffeeA">拿铁</name>
        <price>25</price>
    </coffee>
</bookstore>
"""

# 把xml格式的字符串 转化为一个树形结构
root = etree.XML(xmlStr)

# . = /bookstore
# 通配某一个节点下的所有子标签
# result = root.xpath('./*')
# result = root.xpath('//book | //coffee | //time')


# contains 包含判断  符合标签名之后 判断某一个属性是否包含一个字符串
# . = [contains(text() + @*,"学习")]
# result = root.xpath('//name[contains(text(),"学习")]')
#
# for tag in result:
#     try:
#         # 把对象 字符串化
#         print(etree.tostring(tag).decode())
#     except:
#         print(tag)