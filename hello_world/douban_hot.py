import requests
import re
import jieba
from bs4 import BeautifulSoup
import pandas as pd
import numpy
import matplotlib.pyplot as plt
# % matplotlib inline

import matplotlib

matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)
from wordcloud import WordCloud  # 词云包

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
}


def catch_film():
    film_data = requests.get('https://movie.douban.com/cinema/nowplaying/fuzhou/')
    film_data_html = film_data.text
    # print(film_data_html)
    soup_film_data_html = BeautifulSoup(film_data_html, 'lxml')
    nowplaying_movie = soup_film_data_html.find_all('div', id='nowplaying')
    nowplaying_movie_info = nowplaying_movie[0].find_all('li', class_='list-item')
    nowplaying_movie_info_list = []
    for item in nowplaying_movie_info:
        nowplaying_movie_dict = {}
        nowplaying_movie_dict['id'] = item['id']
        for tag_img_item in item.find_all('img'):
            nowplaying_movie_dict['name'] = tag_img_item['alt']
            nowplaying_movie_info_list.append(nowplaying_movie_dict)
    # print(nowplaying_movie_info_list)
    catch_film_comments(nowplaying_movie_info_list)

def catch_film_comments(list):
    for id in list:
        comments_requrl = 'https://movie.douban.com/subject/' + id['id'] + '/comments' + '?' + 'start=P'
        comments_data = requests.get(comments_requrl)
        soup_comments_data  = BeautifulSoup( comments_data.text, 'lxml')
        comments_data_info = soup_comments_data.find_all('div', class_='comment-item')
        comments_data_info_list = []
        for item in comments_data_info:
            if item.find_all('p')[0].string is not None:
                comments_data_info_list.append(item.find_all('p')[0].string)
        print(id['name']+'热点词云:\n')
        word_count(comments_data_info_list)

def word_count(list):
    comments = ''
    for k in range(len(list)):
        comments = comments + (str(list[k])).strip()
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    filterdata = re.findall(pattern, comments)
    cleaned_comments = ''.join(filterdata)
    segment = jieba.lcut(cleaned_comments)
    words_df = pd.DataFrame({'segment': segment})
    # print(words_df)
    stopwords = pd.read_csv("chineseStopWords.txt", index_col=False, quoting=3, sep="\t", names=['stopword'],encoding='utf-8')  # quoting=3全不引用
    words_df = words_df[~words_df.segment.isin(stopwords.stopword)]
    # print(words_df)
    words_stat = words_df.groupby(by=['segment'])['segment'].agg({"计数": numpy.size})
    words_stat = words_stat.reset_index().sort_values(by=["计数"], ascending=False)
    # print(words_stat)
    ciyun_maker(words_stat)

def ciyun_maker(word):
    wordcloud = WordCloud(font_path="simhei.ttf", background_color="white", max_font_size=80)  # 指定字体类型、字体大小和字体颜色
    word_frequence = {x[0]: x[1] for x in word.head(1000).values}
    word_frequence_list = []
    for key in word_frequence:
        temp = (key, word_frequence[key])
        word_frequence_list.append(temp)

    wordcloud = wordcloud.fit_words(word_frequence_list)
    plt.imshow(wordcloud)

if __name__ == '__main__':
    catch_film()