# coding:utf-8
import cookielib
import mechanize
import urllib
from lxml import etree

all_data = [['username1', 'password1'], ['username2', 'password2']]
for i in all_data:
    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)
    br.open('http://k4w.cn/user/index.html')
    br.select_form(nr=0)
    br.form['mail'] = i[0]
    br.form['password'] = i[1]
    br.submit()
    response = br.open('http://k4w.cn/level_search/1/78/0/0/0.html')
    parameters = {'z_data' : '10',
                  'id' : '99',
                  'sid' : '78'
                 }              #  POST data
    data = urllib.urlencode(parameters)
    response = br.open('http://k4w.cn/zone/z_num.html', data)
    print "%s 投票成功！" % i[0]
br = mechanize.Browser()
response = br.open('http://k4w.cn/level_search/1/78/0/0/0.html')
page = etree.HTML(response.read().lower().decode('utf-8'))
hrefs = page.xpath(u"//span[@class='number n_99']")
print "当前票数：" + hrefs[0].text