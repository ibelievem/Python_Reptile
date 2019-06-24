from selenium import webdriver
import fake_useragent


# 谷歌的设置
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"')
driver = webdriver.Chrome(chrome_options=chromeOptions)
driver.get('http://service.spiritsoft.cn/ua.html')
print(driver.page_source)
driver.save_screenshot("./谷歌UA截图.png")


# 火狐的设置
# # ua配置对象
# profile = webdriver.FirefoxProfile()
# user_agent = fake_useragent.FakeUserAgent().random
# # 修改ua
# profile.set_preference("general.useragent.override", user_agent)
# # 保存设置
# profile.update_preferences()
#
# driver = webdriver.Firefox(firefox_profile=profile)
# driver.get('http://service.spiritsoft.cn/ua.html')
# print(driver.page_source)
