import re
import requests

html = requests.get("https://www.qiushibaike.com/8hr/page/13/")
str = html.text
titleList = re.findall('<a.*?class="recmd-content".*?>.*?</a>',str)
userNameList = re.findall('<span .*?class="recmd-name">.*?</span>',str)
likeAndCommentList = re.findall('<div class="recmd-num">.*?</div>',str,re.S)
for index in range(len(titleList)):
    title = re.findall('">(.*?)</a>',titleList[index])[0]
    url = re.findall('href="(.*?)"',titleList[index])[0]
    userName = re.findall('">(.*?)</span>',userNameList[index])[0]
    infoList = re.findall('<span>(.*?)</span>',likeAndCommentList[index],re.S)
    length = len(infoList)
    if(length == 5):
        like = infoList[0]
        comment = infoList[3]
    elif(length == 2):
        like = infoList[0]
        comment = "0"
    elif(length == 0):
        like = "0"
        comment = "0"
    print(title,url,userName,like,comment)




