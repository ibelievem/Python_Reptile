import requests
import re

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
}
html = requests.get("http://www.baidu.com",headers=headers).content.decode()
print(html)
# 匹配title标签之间的文本值 title没有任何其他属性干扰
pattern = re.compile("<title>(.*?)</title>")
print(pattern.search(html).group(1))