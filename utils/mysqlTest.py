#!/usr/bin/python
# coding:utf-8
import MySQLdb
import json

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='root',
        db ='oa',
        charset="UTF8"
        )

cur = conn.cursor();

print("连接成功！");

#插入一条数据,修改删除也是用这个方法
# sqli="insert into student values(%s,%s,%s,%s)"
# cur.execute(sqli,('3','Huhu','2 year 1 class','7'))

#一次插入多条记录
# sqli="insert into student values(%s,%s,%s,%s)"
# cur.executemany(sqli,[
#     ('3','Tom','1 year 1 class','6'),
#     ('3','Jack','2 year 1 class','7'),
#     ('3','Yaheng','2 year 2 class','7'),
#     ])

# 读取数据
sqls = "SELECT * FROM intention_work"
rsCount = cur.execute(sqls)

print(rsCount)

result = cur.fetchmany(rsCount);

for temp in result:
    print(json.dumps(temp).decode("unicode-escape"))

cur.close();
conn.commit();
conn.close();
