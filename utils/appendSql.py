#!/usr/bin/python
# coding:utf-8
import os


#############临时通过mid列表查询umid列表###############


ids = []
filename='mids.txt'

if os.path.exists(filename):
    f = open(filename, "rb")
    while True:
        line = f.readline()
        if not line:
            break
        line = line.replace("\n", "")
        ids.append(line)
        # join：用分隔符连接字符串
    print "SELECT id,name FROM table WHERE id IN (" + ",".join(ids) + ")"
