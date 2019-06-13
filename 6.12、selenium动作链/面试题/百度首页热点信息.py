# 爬取百度首页热点新闻 每次取10条 需使用requests+lxml 提取

import requests
from lxml import etree
import re

headers = {
    "Host":"www.baidu.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept":"text/plain, */*; q=0.01",
    "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding":"gzip, deflate, br",
    "Referer":"https://www.baidu.com/",
    "X-Requested-With":"XMLHttpRequest",
    "Connection":"keep-alive",
}

cookies = {
    "_ga":"GA1.2.783538125.1560253198",
    "_gid":"GA1.2.1232689475.1560253198",
    "BAIDUID":"4F34292CCAAB053286E0B69EB3C2A668:SL=0:NR=10:FG=1",
    "BD_HOME":"1",
    "BD_UPN":"13314752",
    "bdime":"0",
    "BDORZ":"FFFB88E999055A3F8A630C64834BD6D0",
    "BDUSS":"pYRmNPQnFyRHRMUEJubjBraWRDSmY3c05DeTFyOTgxZUxlWlV-fkNjdlVJaWRkSVFBQUFBJCQAAAAAAAAAAAEAAACfr9CR98jX5U1YWFlaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANSV~1zUlf9cZX",
    "BIDUPSID":"1199C147E9C1ED132FFA7597FE1B74BC",
    "COOKIE_SESSION":"4_0_8_4_1_4_0_0_7_3_0_0_1560253187_0_2_0_1560253304_0_1560253302|9#343579_18_1560070677|9",
    "delPer":"0",
    "H_PS_645EC":"acf2fYe1Gv1BJJc98OBWwHpX3Qcv/ma46pliWGB6nOMPNjDHZtkAND0a7Moh5OL1uZn0",
    "H_PS_PSSID":"1454_21110_29135_29238_28518_29098_28833_26350_29132",
    "ispeed_lsm":"2",
    "MCITY":"-:",
    "ORIGIN":"0",
    "PSTM":"1505117195",
    "sug":"0",
    "sugstore":"0",
}

params = {
    "id": "2",
    "offset": "0",
    "sessionId": "15602539100609",
    "crids": "",
    "version": "",
    "pos": "0",
    "newsNum": "0",
    "blacklist_timestamp": "0",
    "indextype": "manht",
    "_req_seqid": "0xfd2dfd600005324c",
    "asyn": "1",
    "t": "1560253925401",
    "sid": "1454_21110_29135_29238_28518_29098_28833_26350_29132",
}

info={}
while(len(info)!=10):
    res = requests.get("https://www.baidu.com/home/pcweb/data/mancardwater",params=params,headers=headers,cookies=cookies).content.decode()
    print(res)
    htmlStr = re.search('"html" : "(.*)","isEnd"',res,re.S).group(1)
    print(htmlStr)
    root = etree.HTML(htmlStr)
    titles = root.xpath('//a[@class="s-title-yahei"]/text()')
    hrefs = root.xpath('//a[@class="s-title-yahei"]/@href')
    print(len(titles))
    print(titles)
    print(len(hrefs))
    print(hrefs)
    for i in range(len(titles)):
        info[titles[i]]=hrefs[i][4:]
        if(len(info) == 10):
            break
print(info)
with open("./info.csv","w",encoding="utf-8") as f:
    for i in info.keys():
        str = i + "," + info[i] + "\n"
        f.write(str)

