# -*- coding: utf-8 -*-
import pymysql

conn = pymysql.connect(host='106.14.220.77',user='root',passwd='123456',db='mydb',port=3306,charset='utf8')
cursor = conn.cursor()
cursor.execute("insert into test (name,sex,grade) values(%s,%s,%s)",('张三','女', 87))
conn.commit()