from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://tech.163.com/")

for i in range(3):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)

newsList = driver.find_elements_by_xpath("//div[@class='data_row news_article clearfix']")
print(len(newsList))

for news in newsList:
    imgSrc = news.find_element_by_xpath("./a/img").get_attribute("src")
    print(imgSrc)
    title = news.find_element_by_xpath("./div/div/h3/a").text
    print(title)
    tag = news.find_element_by_xpath("./div/div/strong/a").text
    print(tag)
    kws = news.find_elements_by_xpath("./div/div/div/a")
    for kw in kws:
        print(kw.text)
    comment = news.find_element_by_xpath("./div/div/a/div/span").text
    print(comment)
    # js 滚动到某一个元素
    driver.execute_script("arguments[0].scrollIntoView(false);", news)

