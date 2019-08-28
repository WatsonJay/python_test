import base64
import datetime
import requests
from lxml import etree
import os
import shutil
import time
from hello_world import free_proxyIP

# 全局变量
token = ''

urls = ['https://bcy.net/apiv3/rank/list/itemInfo?p={}&ttype=cos&sub_type=week&date={}'.format(str(i),datetime.datetime.now().strftime('%Y%m%d')) for i in range(1, 10)]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'
}
def get_info_url(url):
    is_exists = os.path.exists("./bcy-cos")
    # 判断结果
    if not is_exists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs("./bcy-cos")
    ip = free_proxyIP.proxyip()
    Proxy_Ip = {'http': ip}
    list = requests.get(url, headers=headers, proxies=Proxy_Ip, timeout=3)
    data = list.json()
    for page in data['data']['top_list_item_info']:
        detail_url = "https://bcy.net/item/detail/{}?_source_page=charts".format(page['since'])
        cover_pic_url = page['item_detail']['cover']
        pic_base64 = base64.b64encode(requests.get(cover_pic_url).content)
        is_pass = face_detective(pic_base64,token)
        if is_pass:
            get_page_url(detail_url)

def get_page_url(url):
    ip = free_proxyIP.proxyip()
    Proxy_Ip = {'http': ip}
    list = requests.get(url, headers=headers, proxies=Proxy_Ip, timeout=3)
    selector = etree.HTML(list.text)
    pic_url = selector.xpath('//div[@class="img-wrap-inner"]/img/@src')
    print(pic_url)

def get_token(api_key,secret_key):
    # 获取token
    URL = "https://aip.baidubce.com/oauth/2.0/token"
    params = {
        "grant_type": "client_credentials",
        "client_id": api_key,
        "client_secret": secret_key
    }
    s = requests.post(URL, data=params)
    token = s.json().get('access_token')
    return token

def face_detective(image_base64, token):
    # 人脸检测
    URL = "https://aip.baidubce.com/rest/2.0/face/v3/detect"

    params = {
        "face_field": "age,gender,beauty,qualities",
        "image_type": "BASE64",
        "image": image_base64,
    }

    url = URL + "?access_token=" + token
    response = requests.post(url, data=params)

    r = response.json().get('result')
    is_pass = process_face_data(r)
    return is_pass


def process_face_data(r):
    # 筛选美女
    if r is None or r["face_num"] != 1:
        return False
    else:
        face = r["face_list"][0]
        if face["face_probability"] > 0.7 and face["beauty"] > 70 and face["gender"]["type"] == "female":
            return True
        else:
            return False


if __name__ == '__main__':
    # 百度AI 申请信息   API Key, Secret Key
    API_KEY = "M0I0tLQinBM1mS4Wz97WgVp4"
    SECRET_KEY = "7qKQE9EEf97dSO9jzqouMTmfBVDfSIvY"
    token = get_token(API_KEY,SECRET_KEY)
    for url in urls:
        get_info_url(url)