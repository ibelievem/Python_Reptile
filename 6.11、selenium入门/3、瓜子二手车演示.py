import requests
from selenium import webdriver

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
}
html = requests.get("https://www.guazi.com/zz/?ca_s=pz_baidu&ca_n=tbmkbturl&scode=10103000312",headers=headers).content.decode()
print(html)


print("========================================")



driver=webdriver.Firefox()
driver.get("https://www.guazi.com/zz")
print(driver.page_source)

