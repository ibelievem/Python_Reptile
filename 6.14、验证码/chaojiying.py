#!/usr/bin/env python
# coding:utf-8

import requests
from hashlib import md5
from selenium import webdriver
from PIL import Image
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password =  password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()


if __name__ == '__main__':

    driver = webdriver.Firefox()
    driver.get("https://kyfw.12306.cn/otn/login/init")
    driver.implicitly_wait(20)
    driver.maximize_window()

    sleep(5)
    logoElement = driver.find_element_by_xpath('//img[@class="touclick-image"]')
    # 相对于浏览器左上角的像素位置
    print(logoElement.location)
    print(logoElement.size)
    driver.save_screenshot("./12306.png")
    # 求图片矩形区域的边界
    left = logoElement.location["x"]
    top = logoElement.location["y"]
    right = left + logoElement.size["width"]
    bottom = top + logoElement.size["height"]
    print(left, top, right, bottom)
    bd = Image.open("./12306.png")
    # 根据左上右下四个边界 进行剪裁
    logo = bd.crop((left, top, right, bottom))
    logo.save("./12306checkCode.png")

    # 第三方提供的服务
    # 帐户名 密码 softID
    chaojiying = Chaojiying_Client('935528334', '123456', '899506')
    # 处理的图片
    im = open('./12306checkCode.png', 'rb').read()
    # 和服务器交互 传指定的图片与验证码类型
    checkCodeRes = chaojiying.PostPic(im, 9004)
    clickPositions = checkCodeRes["pic_str"].split("|")
    print(clickPositions)

    for position in clickPositions:
        xy = position.split(",")
        # 移动到验证密码元素 然后偏移 # 信息取出xy信息做偏移
        ActionChains(driver).move_to_element_with_offset(logoElement,int(xy[0]),int(xy[1])).click().perform()
        sleep(1)


