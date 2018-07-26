import requests
import re
import jieba  #分词包
import time
from bs4 import BeautifulSoup
import pandas as pd
import numpy  #numpy计算包
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)
from wordcloud import WordCloud  # 词云包

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
}


def catch_film():
    film_data = requests.get('https://movie.douban.com/cinema/nowplaying/fuzhou/',headers=headers) #抓取电影热门排行
    film_data_html = film_data.text
    soup_film_data_html = BeautifulSoup(film_data_html, 'lxml') #soup 解析
    nowplaying_movie = soup_film_data_html.find_all('div', id='nowplaying')
    nowplaying_movie_info = nowplaying_movie[0].find_all('li', class_='list-item')
    nowplaying_movie_info_list = []
    for item in nowplaying_movie_info:
        nowplaying_movie_dict = {}
        nowplaying_movie_dict['id'] = item['id']
        for tag_img_item in item.find_all('img'):
            nowplaying_movie_dict['name'] = tag_img_item['alt']
            nowplaying_movie_info_list.append(nowplaying_movie_dict)
    catch_film_comments(nowplaying_movie_info_list)

def catch_film_comments(list):
    for id in list:
        print('构造'+id['name'] + '热点词云\n')
        comments_data_info_list_total = []
        for i in range(1,11):  #获取前10页评论
            comments_data_info_list_temp=catch_file_comment_per_page(id,i)
            comments_data_info_list_total.append(comments_data_info_list_temp)
        print(id['name']+'热点词云:\n')
        word_count(comments_data_info_list_total,id['name'])

def catch_file_comment_per_page(id,i):
    comments_data_info_list = []
    if i>0:
        comments_requrl = 'https://movie.douban.com/subject/' + id['id'] + '/comments' + '?' + 'start=' + str((i - 1) * 20) + '&limit=20' #获取每页20个评论
        print('正在爬取:'+comments_requrl)
        comments_data = requests.get(comments_requrl, headers=headers)
        soup_comments_data = BeautifulSoup(comments_data.text, 'lxml')
        comments_data_info = soup_comments_data.find_all('div', class_='comment-item')
        for item in comments_data_info:
            if item.find_all('p') != []:
                if item.find_all('p')[0].string is not None:
                    comments_data_info_list.append(item.find_all('p')[0].string)
        time.sleep(1)
        return comments_data_info_list

def word_count(list,id):
    comments = ''
    for k in range(len(list)):
        comments = comments + (str(list[k])).strip()
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    filterdata = re.findall(pattern, comments)
    cleaned_comments = ''.join(filterdata)  #删除标点符号
    segment = jieba.lcut(cleaned_comments)    #分词
    words_df = pd.DataFrame({'segment': segment})
    stopwords = pd.read_csv("chineseStopWords.txt", index_col=False, quoting=3, sep="\t", names=['stopword'],encoding='utf-8')  # quoting=3全不引用
    words_df = words_df[~words_df.segment.isin(stopwords.stopword)]
    words_stat = words_df.groupby(by=['segment'])['segment'].agg({"计数": numpy.size})
    words_stat = words_stat.reset_index().sort_values(by=["计数"], ascending=False)  #频度统计
    ciyun_maker(words_stat,id)

def ciyun_maker(word,id):
    wordcloud = WordCloud(font_path="loli.ttf", background_color="white", max_font_size=80)  # 指定字体类型、字体大小和字体颜色
    word_frequence = {x[0]: x[1] for x in word.head(1000).values}
    wordcloud = wordcloud.fit_words(word_frequence)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    wordcloud.to_file('F:/python/python_test/hello_world/picture/'+id+'热点词云.png')

if __name__ == '__main__':
    print('[INFO]:douban(豆瓣) hot film wordcloud...')
    print('[Version]: V1.0')
    print('[Author]: 花二爷')
    catch_film()