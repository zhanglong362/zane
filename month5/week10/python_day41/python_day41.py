# -*- encoding: utf-8 -*-

import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123456',
    database='db1',
    charset='utf8'
)

cursor = conn.cursor(pymysql.cursor.DictCursor)

rows = cursor.callproc('p1', (2,4,1))
print('rows: %s' % rows)
data = cursor.fetchall()
print('data: %s' % data)

cursor.close()
conn.close()