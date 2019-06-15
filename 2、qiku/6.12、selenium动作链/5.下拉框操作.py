from selenium import webdriver
from time import sleep
# 导入一个下拉框类
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.get("http://sahitest.com/demo/selectTest.htm")
sleep(3)

# 下拉框操作 需要提前构造 Select类 参数：select标签元素
select = Select(driver.find_element_by_xpath("//select[@id='s1Id']"))
# 通过索引
select.select_by_index(1)
sleep(3)
# 通过value属性值
select.select_by_value("o2")
sleep(3)
# 通过innerHTML 内部文本值
select.select_by_visible_text("o3")
sleep(3)
