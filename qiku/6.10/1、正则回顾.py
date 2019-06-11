import re

# #1、macth的正则实现与字符串的实现
# #处理目标字符串
# str='hello world'
#
# #定义一种规则，进行切片、替换、切割
# pattren=re.compile('he')
#
# #处理目的 选择不同的函数 切片：match、search、findall
# #替换：sub  切割：split
# print(re.match(pattren, str))
#
# print(str.startswith("he"))
# print(len('he'))




# =================================================
# #macth的正则实现与字符串的实现
# #处理目标字符串
# str='hello world'
#
# #定义一种规则，进行切片、替换、切割
# pattren=re.compile('he')
#
# #处理目的 选择不同的函数 切片：match、search、findall
# #替换：sub  切割：split
# print(re.match(pattren, str))
#
# print(str.find("el"))
# print(len('el'))



# ==========================================
# # # sub 的正则实现与字符串的实现
#
# str='hello world'
#
# #定义一种规则，进行切片、替换、切割
# pattren=re.compile('l')
#
# #处理目的 选择不同的函数 切片：match、search、findall
# #替换：sub  切割：split
# print(re.sub(pattren, "*",str))
# print(str.replace("l","*"))



# =================================================
# # # spilt 的正则实现与字符串的实现
#
# str='hello world'
#
# #定义一种规则，进行切片、替换、切割
# pattren=re.compile('l')
#
# #处理目的 选择不同的函数 切片：match、search、findall
# #替换：sub  切割：split
# print(re.split(pattren,str))
# print(str.split("l"))





# =======================================

str = "abbbbbbc"

# 贪婪模式
# * 决定了尽可能的多匹配b，结果是a，取得最小值
pattern = re.compile(r"ab*")
print(pattern.match(str).group())

# 非贪婪模式
# *? 决定了尽可能少匹配b，结果是a
pattern = re.compile(r"ab*?")
print(pattern.match(str).group())

# 至少匹配一次，结果是ab
pattern = re.compile(r"ab+?")
print(pattern.match(str).group())






