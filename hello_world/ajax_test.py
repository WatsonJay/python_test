import requests
from lxml import etree
import pymongo

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
}

client = pymongo.MongoClient('106.14.220.77',27017)
mydb = client['mydb']
timeline = mydb['timeline']

def get_time_info(url,page):
    url_split = url.split('/')
    user_id = url_split[4]
    if url.find('page='):
        page = page + 1
    html = requests.get(url, verify=True, headers=headers)
    selector = etree.HTML(html.text)
    infos  = selector.xpath('//ul[@class="note-list"]/li')
    for info in infos:
        date = info.xpath('div/div/div/span/@data-datetime')[0]
        type = info.xpath('div/div/div/span/@data-type')[0]
        timeline.insert_one({'date':date,'type':type})
    id_infos = selector.xpath('//ul[@class="note-list"]/li/@id')
    if len(infos) > 1:
        feed_id = id_infos[-1]
        max_id = str(int(feed_id.split('-')[1])-1)
        next_url = 'https://www.jianshu.com/users/%s/timeline?max_id=%s&page=%s' %(user_id, max_id, page)
        get_time_info(next_url, page)

if __name__ == '__main__':
    get_time_info('https://www.jianshu.com/users/e4aec3c9fc3f/timeline',1)