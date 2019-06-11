from urllib import request
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

url = "https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
ua = UserAgent()
rua = ua.random
print(rua)
headers = {
    "User-Agent":rua
}
response = request.urlopen(url)
html = response.read()
print(html)
soup = BeautifulSoup(html,"lxml")
positionList = soup.select("div[class='el']>p>span>a")
companyList = soup.select("div[class='el']>span[class='t2']>a")
cityList = soup.select("div[class='el']>span[class='t3']")
salaryList = soup.select("div[class='el']>span[class='t4']")
dateList = soup.select("div[class='el']>span[class='t5']")
for x in range(len(positionList)):
    print(positionList[x]['title'])
    print(companyList[x]['title'])
    print(cityList[x].string)
    print(salaryList[x].string)
    print(dateList[x].string)