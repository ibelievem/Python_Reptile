# 编码 和 解码

#编码
str="今天是个好日子"
#转化为utf-8编码
strEncode=str.encode()
print(strEncode,type(strEncode))


#解码

decodeResult=strEncode.decode()
print(decodeResult,type(decodeResult))