import ssl
from urllib import parse

import requests
from lxml import etree

# 取消代理验证
ssl._create_default_https_context = ssl._create_unverified_context

def searchingflim(name,page):
    # 将文本转为 gb2312 编码格式
    name = parse.quote(name.encode('gb2312'))
    #引入url头格式
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }
    #参数化url
    url = "https://www.meijutt.com/search/index.asp?page={}&searchword={}&searchtype=-1"
    #请求页面
    try:
        reponse = requests.get(url, headers=headers)
        if reponse.status_code == 200:
            return reponse.text
        else:
            return None
    except requests.RequestException:
        return None


if __name__ == '__main__':
    #check()
    #proxyip()
    searchingflim("绿箭侠")