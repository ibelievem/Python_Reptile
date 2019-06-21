# *     [0,无穷]
# +     [1，无穷]
# ？     [0,1]

# 字符串匹配有三种方法：
# 1、将正则表达式编译为对象，通过对象对文本进行匹配查找
# 2、直接查找字符串   re.函数("正则表达式","匹配字符串")
# 3、不使用正则，直接使用字符串的方法

import re

# # macth的正则实现与字符串库实现
# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，
# 则匹配失败，函数返回None；

# 方法一：
# # 1、目标字符串
# str = "hello world"

# # 2、将正则表达式编译成 Pattern 对象
# pattern = re.compile("he")

# # 3、处理目的 选择不同的函数   切片：match,search,findall
# #                           替换：sub 切割：split
# result=pattern.match(str)
# print(result)

# 方法二：
# 1、目标字符串
# str = "hello world"

# 2、处理目的 选择不同的函数   切片：match,search,findall
#                           替换：sub 切割：split
# result=re.match("he",str)
# print(result)
# =======================================================

# # search 的正则实现与字符串库实现
# re.search匹配整个字符串，直到找到一个匹配。

# # 1、目标字符串
# str = "hello world"

# # 2、将正则表达式编译成 Pattern 对象
# pattern = re.compile("he")

# # 3、处理目的 选择不同的函数 切片：match,search,findall
# # 替换：sub 切割：split

# result=pattern.search(str)
# print(result)


# =======================================================

# # findall的正则实现与字符串库实现
# 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，
# 如果没有找到匹配的，则返回空列表

# # 1、目标字符串
# str = "hello world"

# # 2、将正则表达式编译成 Pattern 对象
# pattern = re.compile("l")

# # 3、处理目的 选择不同的函数 切片：match,search,findall
# # 替换：sub 切割：split

# result=pattern.findall(str)
# print(result)

# =============================================

# # sub的正则实现与字符串库实现

# # 1、目标字符串
# str = "hello world"

# # 2、将正则表达式编译成 Pattern 对象
# pattern = re.compile("l")

# # 3、处理目的 选择不同的函数 切片：match,search,findall
# # 替换：sub 切割：split
# 将字符串中的l替换为*
# result=pattern.sub("*",str)
# print(result)

# ================================================

# # spilt的正则实现与字符串库实现

# # 1、目标字符串
# str = "hello world"
#
# # # 2、将正则表达式编译成 Pattern 对象
# pattern = re.compile("l")
#
# # # 3、处理目的 选择不同的函数 切片：match,search,findall
# # # 替换：sub 切割：split
# result=pattern.split(str)
# print(result)



# =================================================

# 【贪婪模式和非贪婪模式】
# 贪婪模式：在整个表达式匹配成功的前提下，尽可能多的匹配 ( * )；
# 非贪婪模式：在整个表达式匹配成功的前提下，尽可能少的匹配 ( ? )；
# Python里数量词默认是贪婪的

# 例一、
# str = "abbbbbbc"

# # 贪婪模式
# # * 决定了尽可能多匹配 b，所以a后面所有的 b 都出现了。
# pattern = re.compile(r"ab*")
# print(pattern.match(str).group())


# # 非贪婪模式
# # *? 决定了尽可能少匹配b，结果是a 取得最小值
# pattern = re.compile(r"ab*?")
# print(pattern.match(str).group())

# # 非贪婪模式
# # ? 数量谓语 0 或 1 取的最大值
# pattern = re.compile(r"ab?")
# print(pattern.match(str).group())



# 例二、
str = "<html><div>aa<div>杂乱数据</div><span>目标数据</span></div><div>bb</div></html>"

# # 贪婪模式
# # 尽可能的多匹配 找到最后一个</div>为后边界
# <html>.*</html>
# re.S 使.匹配包括换行在内的所有字符
# pattern = re.compile("<div>.*</div>",re.S)
# print(pattern.findall(str))


# # 非贪婪模式
# # 尽可能的少匹配 找到第一个</div>为后边界
pattern = re.compile("<div>.*?</div>",re.S)
print(pattern.findall(str))
# print(re.findall("<div>.*?</span>",str,re.S))



