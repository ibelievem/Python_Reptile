from selenium import webdriver
from selenium.webdriver.common.by import By


# str = requets.get("url").content.decode()
# root = etrr.HTML(str)
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

# 通过类名查找元素
# single = driver.find_element_by_class_name("mnav")
# double = driver.find_elements_by_class_name("mnav")
# # 元素.text 获取内部文本值
# print(single.text)
# print("===========================")
# for item in double:
#     print(item.text)

# 通过name属性查找元素 元素.get_attribute("属性名")
# print(driver.find_element_by_name("tj_trhao123").text)
# print(driver.find_element_by_name("tj_trhao123").get_attribute("href"))

# 通过链接文本值查找 find_element_by_link_text 文本值和参数相等
#find_element_by_partial_link_text 文本值包含参数
# print(driver.find_element_by_link_text("地图").get_attribute("href"))
# print(driver.find_element_by_partial_link_text("地").get_attribute("href"))
# tagList = driver.find_elements_by_partial_link_text("百度")
# for tag in tagList:
#     print(tag.get_attribute("href"))

# 通过id属性查找
# print(driver.find_element_by_id("form").get_attribute("class"))
# 通过标签名查找
# print(driver.find_element_by_tag_name("form").get_attribute("class"))

# 使用xpath获取 路径写到元素这一级就可以了 写到取文本取属性 有异常
single = driver.find_element_by_xpath('//*[@class="mnav"]/@href')
print(single)
single = driver.find_element_by_xpath('//*[@class="mnav"]/text()')
print(single)


# double = driver.find_elements_by_xpath('//*[@class="mnav"]')
# # 元素.text 获取内部文本值
# print(single.text)
# print("===========================")
# for item in double:
#     print(item.text)

# single = driver.find_element_by_css_selector('.mnav')
# double = driver.find_elements_by_css_selector('.mnav')
# # 元素.text 获取内部文本值
# print(single.text)
# print("===========================")
# for item in double:
#     print(item.text)

# 特殊方式获取元素
# single = driver.find_element(By.XPATH,'//*[@class="mnav"]')
# print(single.text)

driver.quit()
