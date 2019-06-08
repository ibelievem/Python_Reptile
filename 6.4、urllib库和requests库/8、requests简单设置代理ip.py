import requests

url="http://ip.27399.com/"

proxies={
    "http":"//27.221.32.140:80"
}

html=requests.get(url,proxies=proxies).content.decode()
print(html)






