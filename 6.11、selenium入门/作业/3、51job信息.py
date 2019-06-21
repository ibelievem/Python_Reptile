import requests
from lxml import etree
import chardet

url="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="

response=requests.get(url)

# 将网页转为字节类型
html=response.content

# 为保险，首先应该获取网页的编码格式
encoding=chardet.detect(html)["encoding"]

# 解码为字符串格式
html=html.decode(encoding)

# 构建树形结构
root=etree.HTML(html)

result=root.xpath("//div[@class='dw_table']/div[@class='el']")
print("共有数据：",len(result))

for i in result:
    job_title=i.xpath("./p/span/a/text()")[0].replace(" ", "").replace("\n", "")
    company=i.xpath("./span/a/text()")[0].replace(" ", "").replace("\n", "")
    place=i.xpath("./span[2]/text()")[0]

    salary=i.xpath("./span[3]/text()")
    if len(salary)==0:
        salary=''
    else:
        salary=salary[0]
    date=i.xpath("./span[4]/text()")[0]
    print(job_title,company,place,salary,date)
    with open("data.csv", "a",encoding="utf-8") as w:
        w.writelines([job_title,",",company,",",place,",",salary,",",date])



