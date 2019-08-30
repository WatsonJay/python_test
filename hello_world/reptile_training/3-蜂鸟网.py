import requests
#json解析库,对应到lxml
import json
#json的解析语法，对应到xpath
import jsonpath
from lxml import etree
from hello_world import free_proxyIP

urls = ['https://photo.fengniao.com/ajaxPhoto.php?action=getPhotoLists&fid=403&sort=1&page={}/'.format(str(i)) for i in range(1, 10)]
headers = {'Host': 'photo.fengniao.com',
            'X-Requested-With':'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'
                          }
def get_info_url(url):
    ip = free_proxyIP.proxyip()
    Proxy_Ip = {'http': ip}
    html = requests.get(url, headers=headers, proxies=Proxy_Ip, timeout=3)
    # 把json形式的字符串转换成python形式的Unicode字符串
    unicodestr = json.loads(html.text)
    # python形式的列表
    pic_list = jsonpath.jsonpath(unicodestr, "$..picUrl")
    print(1)

if __name__ == '__main__':
    for url in urls:
        get_info_url(url)