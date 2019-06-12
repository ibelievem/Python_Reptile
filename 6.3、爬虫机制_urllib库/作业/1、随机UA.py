# 1.编写一个UserAgent的配置文件，实现配置文件的读取以及
# 有一个函数可以获取一个随机UserAgent用用户身份代理


from urllib import request
import random

#1、读取配置
with open("./UAConfig.txt") as r_f:
    data=r_f.read()

    #分割之后拿到每一行的数据
    lines=data.split("\n")
    for i in lines:
        print(i)

#2、随机
userAgent=random.choice(lines)

print(len(lines))
print(userAgent)
