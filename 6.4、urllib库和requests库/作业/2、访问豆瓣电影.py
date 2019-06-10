import requests

#设置计数序号
counter=0

url="https://movie.douban.com/j/chart/top_list?"

for i in range(100,0,-10):
    start=0
    while True:
        parameter={
            'type':'11',
            'interval_id':str(i)+":"+str(i-10),
            'action':'',
            'start':start,
            'limit':'20',
        }
        start+=20
        result=requests.get(url,params=parameter).json()
        print(result)

        #当取到最后一页时，跳出循环
        if len(result)==0:
            break

        # item是一个字典
        for item in result:
            title=item['title']
            score=item['score']
            vote_count=item['vote_count']
            counter+=1
            print(counter,title,score,vote_count)
