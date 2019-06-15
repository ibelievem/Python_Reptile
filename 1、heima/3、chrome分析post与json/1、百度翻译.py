import requests

class BaiduFanyi:
    def __init__(self,trans_str):
        self.trans_str=trans_str
        self.lang_detect_url="https://fanyi.baidu.com/langdetect"

    def parse_url(self,url,data):
        requests.post(url,data)


    #实现主要逻辑
    def run(self):
        # 1、获取语言类型
            # 1.1、准备post的url地址，post_data
            lang_detect_data={"query":self.trans_str}
            # 1.2、发送post请求，获取响应
            # 1.3、提取语言类型
        # 2、准备post的数据
        # 3、发送请求，获取响应
        # 4、提取翻译的结果


if __name__ == '__main__':
    baidu_fanyi=BaiduFanyi()
    baidu_fanyi.run()
