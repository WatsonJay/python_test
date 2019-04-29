import ssl
from urllib import parse

import requests
from lxml import etree

# 取消代理验证
ssl._create_default_https_context = ssl._create_unverified_context
#引入url头格式
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }
#参数化url
url_search = "/search/index.asp?page={}&searchword={}&searchtype=-1"
url_head = "https://www.meijutt.com"

def searchingflim(name,page):
    # 将文本转为 gb2312 编码格式
    name = parse.quote(name.encode('gb2312'))
    #请求页面
    try:
        reponse = requests.get(url_head+url_search.format(page,name), headers=headers)
        reponse.encoding = 'gb2312'
        selector = etree.HTML(reponse.text)
        pageinfo = selector.xpath('//div[@class="page"][1]/span/text()')
        if pageinfo:
            if page=="":
                pages = pageinfo[0].split('/')[1].rstrip("页")
                return pages
            else:
                filmList = listfilm(selector)
                return filmList
        else:
            return "no such film"
        if reponse.status_code == 200:
            return reponse.text
        else:
            return "connect false"
    except requests.RequestException:
        return "connect false"

def listfilm(selector):
    # 获取每一季的内容（剧名和链接）
    node_list = selector.xpath('//a[@class="B font_14"]')
    filmList = []
    for node in node_list:
        # 获取信息
        title = node.xpath('@title')[0]
        link = node.xpath('@href')[0]
        film_downpath(link, filmList,title)
    return filmList

def film_downpath(link,filmList,title):
    reponse1 = requests.get(url_head + link, headers=headers)
    reponse1.encoding = 'gb2312'
    downPath = etree.HTML(reponse1.text)
    paths = downPath.xpath('//div[@class="tabs-list current-tab"]//li/p')
    index = 1
    for path in paths:
        items = {}
        items["title"] = title
        if len(path.xpath('./em/text()'))==0:
            items["size"] = "未知大小"
        else:
            items["size"] = path.xpath('./em/text()')[0].strip("[]")
        items["jishu"] = index
        items["link"] = path.xpath('./strong//@href')[0]
        index=index+1
        filmList.append(items)


if __name__ == '__main__':
    #check()
    #proxyip()
    searchingflim("绿箭侠","1")