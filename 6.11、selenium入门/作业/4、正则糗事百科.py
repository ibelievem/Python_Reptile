import requests
import re
import chardet

url="https://www.qiushibaike.com/8hr/page/2/"

response=requests.get(url)

# 将网页转为字节类型
html=response.content


# 为保险，首先应该获取网页的编码格式
encoding=chardet.detect(html)["encoding"]

# 解码为字符串格式
html=html.decode(encoding=encoding)

titleList = re.findall('<a.*?class="recmd-content".*?>(.*?)</a>',html)
print(titleList)


