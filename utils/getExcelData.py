#!/usr/bin/python
# coding:utf-8
import xlrd

try:
    # 使用xlrd打开excel
    data = xlrd.open_workbook('text.xlsx')
    # 通过索引获取第几张表
    table = data.sheets()[0]

    # 获取表的行数
    nrows = table.nrows
    print(nrows)

    # 文件操作
    file = open("mids1.txt","w")
    for x in xrange(1,nrows):
        # 获取单元格
        cell = table.cell_value(x,2)
        print(cell)
        cell = cell.split("_")[1];
        print(cell)
        file.write(cell)
        file.write("\n")
    file.close
except Exception as e:
    print(e)
