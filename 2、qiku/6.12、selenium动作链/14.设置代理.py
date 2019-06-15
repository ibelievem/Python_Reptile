from selenium import webdriver

# profile = webdriver.FirefoxProfile()
#
# profile.set_preference('network.proxy.type', 1)
# profile.set_preference('network.proxy.http', '106.13.117.143')
# profile.set_preference('network.proxy.http_port', 3128)  # int
#
# profile.update_preferences()
#
# driver = webdriver.Firefox(firefox_profile=profile)
# driver.get('http://httpbin.org/ip')
# print(driver.page_source)


chromeOptions = webdriver.ChromeOptions()

# 设置代理
chromeOptions.add_argument("--proxy-server=http://106.13.117.143:3128")
# 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://115.239.240.230:808
browser = webdriver.Chrome(chrome_options = chromeOptions)
# 查看本机ip，查看代理是否起作用
browser.get("http://httpbin.org/ip")
print(browser.page_source)
