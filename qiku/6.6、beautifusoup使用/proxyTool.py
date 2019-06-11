import requests

class ProxyTool:
    @staticmethod
    def GetHtml(url):
        # 蘑菇代理的隧道订单
        appKey = "bEsydTc3OVRGc3BNSWtVSjpyb0NhMmJpU21lZmZ3OFcw"
        # 蘑菇隧道代理服务器地址
        ip_port = 'transfer.mogumiao.com:9001'
        proxy = {
            "http": "http://" + ip_port
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Proxy-Authorization": 'Basic ' + appKey
        }
        r = requests.get(url, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
        print(r.status_code)
        htmlStr = r.content.decode()
        if r.status_code == 302 or r.status_code == 301:
            loc = r.headers['Location']
            url_f = url + loc
            print(loc)
            r = requests.get(url_f, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
            print(r.status_code)
            htmlStr = r.content.decode()
        return htmlStr