from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.guazi.com/zz/buy/")

liList = driver.find_elements_by_xpath("//li[@data-scroll-track]")
for li in liList:
    title = li.find_element_by_xpath(".//h2").text
    info = li.find_element_by_xpath('.//div[@class="t-i"]').text
    price = li.find_element_by_xpath('.//div[@class="t-price"]/p').text
    print(title,"    ",info,"    ",price)
