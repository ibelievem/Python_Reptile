# 加密方式
# 1、时间戳处理
# import time
#
# for i in range(10):
#     time.sleep(2)
#     print(time.time())



# # 2、哈希算法
# import hashlib
# import fake_useragent
#
# # 构建算法规则
# md5 = hashlib.md5()
# ua = fake_useragent.FakeUserAgent().random
# print(ua)
# print(len(ua))
#
# # 传参
# md5.update("a".encode())
# # 取出散列结果
# res = md5.hexdigest()
# print(res)
# print(len(res))


# =============================================
# 解密方式
# 1、执行js
import execjs

jsCode = execjs.compile("""
     js 函数
""")
# jsCode.call("函数名","params")

print(execjs.get().name)
jsCode = execjs.compile("""
    function Add(a,b){
        return a + b;
    };
""")
print(jsCode.call("Add",10,20))




