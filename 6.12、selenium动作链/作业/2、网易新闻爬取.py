from selenium import webdriver
import time

url="https://tech.163.com/"

driver=webdriver.Chrome()

driver.get(url)

time.sleep(1)


# 页面需要向下拉三次到达浏览器底部
for page in range(3):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(0.5)


liList=driver.find_elements_by_xpath("//div[@class='data_row news_article clearfix']")
print(len(liList))

for i in liList:
    # 遍历每一个标签
    # 定位到标签后 使用.text获取文本信息
    imgSrc=i.find_element_by_xpath("./a/img").get_attribute("src")
    title=i.find_element_by_xpath(".//div[@class='news_title']/h3/a").text
    detail=i.find_element_by_xpath('//div[@class="news_tag"]').text.replace("\n","")
    num=i.find_element_by_xpath('.//div[@class="tie-wrap"]/span[2]').text.replace("\n","")
    print(imgSrc,title,detail,num)

    # js 滚动到某一个元素
    driver.execute_script("arguments[0].scrollIntoView(false);", i)


driver.quit()
