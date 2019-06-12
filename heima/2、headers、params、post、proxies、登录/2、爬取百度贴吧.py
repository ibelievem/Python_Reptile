import requests


class Tieba:
    def __init__(self,tieba_name):
        self.tieba_name=tieba_name
        self.url_temp="http://tieba.baidu.com/f?kw=" + tieba_name + "&ie=utf-8&pn={}"
        self.headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"}

    #构造url列表
    def get_url_list(self):
        url_list=[]
        for i in range(1000):
            url_list.append(self.url_temp.format(i*50))
        return url_list

        # return [self.url_temp.format(i * 50) for i in range(1000)]


    #发送请求，获取响应
    def parse_url(self,url):
        print(url)
        response=requests.get(url,headers=self.headers)
        return response.content.decode()


    #保存html字符串
    def save_html(self,html_str,page_num):
        file_path="{},第{}页.html".format(self.tieba_name,page_num)
        print("测试")
        with open(file_path,"w",encoding="utf-8") as f:
            f.write(html_str)

    #实现主要逻辑
    def run(self):
        #1、构造url列表
        url_list=self.get_url_list()
        #2、遍历、发送请求、获取响应
        for url in url_list:
            html_str=self.parse_url(url)
            #3、保存
            #获取url列表中第一个元素的位置，真实的页码数为：元素位置+1
            page_num=url_list.index(url)+1
            self.save_html(html_str,page_num)

if __name__ == '__main__':
    tieba=Tieba("计算机")
    tieba.run()


