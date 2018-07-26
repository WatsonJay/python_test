import requests
from lxml import etree
import csv
import json
import time

fq = open('map/map.csv','wt',newline='',encoding='utf-8')
writer = csv.writer(fq)
writer.writerow(['城市','经度','纬度'])

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
}

def user_url_get():
    url_hots = ['https://www.qiushibaike.com/hot/page/{}/'.format(str(i)) for i in range(1,36)]
    i = 0
    for url_hot in url_hots :
        res =  requests.get(url_hot,headers=headers)
        selector = etree.HTML(res.text)
        url_infos = selector.xpath('//div[@class = "author clearfix"]')
        # print(url_infos)
        for url_info in url_infos :
            user_path_part = url_info.xpath('a[1]/@href')
            if len(user_path_part) == 1 :
                user_url = 'https://www.qiushibaike.com'+ user_path_part[0]
                user_address_get(user_url)
            else:
                pass
        i = i+1
        print('第'+str(i)+'页用户爬取结束')
    print('用户地址爬取结束')

def user_address_get(url):
    user_res = requests.get(url, headers=headers)
    time.sleep(1)
    user_selector = etree.HTML(user_res.text)
    if user_selector.xpath('//div[@class = "user-col-left"]/div[2]/ul/li[4]/text()'):
        address = user_selector.xpath('//div[@class = "user-col-left"]/div[2]/ul/li[4]/text()')
        # print(address)
        if address[0] != '未知':
            user_location(address[0].split(' · ')[1])
        else:
            pass
    else:
        pass

def user_location(address):
    par = {'address': address, 'key': '31d4bf3b17a25cd6db3ec19ab2981ffe'}
    url = 'https://restapi.amap.com/v3/geocode/geo'
    res = requests.get(url, par)
    json_data = json.loads(res.text)
    try:
        location = json_data['geocodes'][0]['location']
        longitude = location.split(',')[0]
        latitude = location.split(',')[1]
        writer.writerow([address, longitude, latitude])
    except IndexError:
        pass
    except KeyError:
        pass

if __name__ == '__main__':
    user_url_get()