from lxml import etree

xmlStr = """
<bookstore>
    <book>
        <name type="python">学习爬虫</name>
        <price>9.9ss</price>
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
        <name type="coffee1">卡布奇洛</name>
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


# 所有的过滤条件都要写在中括号里边[]

# ●按位置进行过滤
# 1、[数字索引] 按索引位置取元素 从1开始的
# result = root.xpath("//coffee[2]")

# 2、[last()] 按索引位置取元素，取最后一个元素
# result = root.xpath("//book[last()]")

# 3、[last()-1] 按索引位置取元素，取倒数第二个元素
# result = root.xpath("//book[last()-1]")

# 4、爬虫数据-json数据处理、[position()>1] 取位置大于1的所有元素
# result = root.xpath("//book[position()>1]")


# ●按属性进行过滤
# 1、选取拥有该属性的元素
# result = root.xpath("//book[@id]")

# 2、获取拥有属性名和属性值的元素
# result = root.xpath('//book[@id="book2"]')

# 3、获取拥有属性名和属性值的元素的内容
# result = root.xpath('//coffee/name[@type="coffee"]/text()')

# 4、爬虫数据-json数据处理、要有子集元素有某一个标签，内部值需要满足可以转化为数字
# 满足不等式
result = root.xpath('//book[price<20]')


for tag in result:
    try:
        # 把对象 字符串化
        print(etree.tostring(tag).decode())
    except:
        print(tag)

