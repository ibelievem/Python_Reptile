import re

# # macth的正则实现与字符串库实现
#
# # 处理目标字符串
# str = "hello world"
# # 定义一种规则 进行切片，替换，切割
# pattern = re.compile("he")
# # 处理目的 选择不同的函数 切片：match,search,findall
# # 替换：sub 切割：split
# print(re.match(pattern,str))
#
# print(str.startswith("he"))
# print(len("he"))

print("=======================================================")
#
# # search macth的正则实现与字符串库实现
# # 处理目标字符串
# str = "hello world"
# # 定义一种规则 进行切片，替换，切割
# pattern = re.compile("el")
# # 处理目的 选择不同的函数 切片：match,search,findall
# # 替换：sub 切割：split
# print(re.search(pattern,str))
#
# print(str.find("el"))
# print(len("el"))

print("=======================================================")

# # findall的正则实现与字符串库实现
# # 处理目标字符串
# str = "hello world"
# # 定义一种规则 进行切片，替换，切割
# pattern = re.compile("l")
# # 处理目的 选择不同的函数 切片：match,search,findall
# # 替换：sub 切割：split
# print(re.findall(pattern,str))

# 遍历计数
# 切割分段

print("=============================================")

# # sub的正则实现与字符串库实现
# str = "hello world"
# # 定义一种规则 进行切片，替换，切割
# pattern = re.compile("l")
# # 处理目的 选择不同的函数 切片：match,search,findall
# # 替换：sub 切割：split
# print(re.sub(pattern,"*",str))
# print(str.replace("l","*"))

print("================================================")

# # spilt的正则实现与字符串库实现
# str = "hello world"
# # 定义一种规则 进行切片，替换，切割
# pattern = re.compile("l")
# # 处理目的 选择不同的函数 切片：match,search,findall
# # 替换：sub 切割：split
# print(re.split(pattern,str))
#
# print(str.split("l"))

# str = "abbbbbbc"
# # 贪婪模式
# # * 决定了尽可能的多匹配b 取的最大值
# pattern = re.compile(r"ab*")
# print(pattern.match(str).group())
#
# # 非贪婪模式
# # *? 决定了尽可能少匹配b，结果是a 取得最小值
# pattern = re.compile(r"ab*?")
# print(pattern.match(str).group())
#
# # 非贪婪模式
# # ? 数量谓语 0 或 1 取的最大值
# pattern = re.compile(r"ab?")
# print(pattern.match(str).group())
#
#
# str = "<html><div>aa<div>杂乱数据</div><span>目标数据</span></div><div>bb</div></html>"
# # 贪婪模式
# # 尽可能的多匹配 找到最后一个</div>为后边界
# # <html>.*<html>
# pattern = re.compile("<div>.*</div>",re.S)
# print(pattern.findall(str))
#
# # 非贪婪模式
# # 尽可能的少匹配 找到第一个</div>为后边界
# pattern = re.compile("<div>.*?</span>",re.S)
# print(pattern.findall(str))
# print(re.findall("<div>.*?</span>",str,re.S))



