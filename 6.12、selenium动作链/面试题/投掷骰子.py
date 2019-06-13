# 同时投掷三个骰子，可能得到的最小点数是3，最大时18，绘制出投掷1000结果的直方图
import matplotlib.pyplot as plt
import random

info = {}
for i in range(10000000):
    sum = 0
    for i in range(3):
        sum = sum + random.randrange(1,7)
    if(info.__contains__(sum)):
        info[sum] = info[sum] + 1
    else:
        info[sum] = 1
print(info)

X = info.keys()
Y = info.values()
plt.rcParams['font.sans-serif']=['SimHei']#正常显示中文汉字
plt.bar(X, Y, 0.4, color="g")
plt.xlabel("结果和")
plt.ylabel("次数")
plt.title("结果和-次数")
plt.show()

