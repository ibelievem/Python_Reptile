from urllib import request

url = 'http://ip.27399.com/'


# 1、构造一个字典传入一个代理地址
proxy = {"http":"106.13.117.143:3128"}

# 2、构建代理地址
proxyHandler = request.ProxyHandler(proxy)

# 3、构造urllib 要求的urlopener打开器
opener = request.build_opener(proxyHandler)

# 4、爬虫数据-json数据处理、进行安装
request.install_opener(opener)


# 构造请求对象
req = request.Request(url)
# 网页请求
html = request.urlopen(req).read()
print(html.decode())