from urllib import request
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

url = "http://zst.aicai.com/ssq/openInfo/"
ua = UserAgent()
rua = ua.random
headers = {
    "User-Agent":rua
}
response = request.urlopen(url)
html = response.read()
soup = BeautifulSoup(html,"lxml")

# //table/tbody/tr
# table>tbody>tr

trList = soup.select(""" tr[onmouseover="this.style.background='#fff7d8'"] """)
for tr in trList:
    for child in tr.contents:
        if(child.name != None):
            print(child.string)