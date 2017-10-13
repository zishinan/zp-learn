#!/usr/bin/python
# coding:utf-8
from selenium import webdriver
import datetime
import time

driver = webdriver.Chrome(executable_path="chromedriver.exe")

def login(uname,pwd):
    driver.get("https://www.jd.com/")
    if driver.find_element_by_link_text("你好，请登录"):
        print('你好，请登录 login ...')
        driver.find_element_by_link_text("你好，请登录").click()
    if driver.find_element_by_link_text("账户登录"):
        print('账户登录 login ...')
        driver.find_element_by_link_text("账户登录").click()
    if driver.find_element_by_name("loginname"):
        print('输入用户名')
        driver.find_element_by_name("loginname").send_keys(uname)
    if driver.find_element_by_name("nloginpwd"):
        print('输入密码')
        driver.find_element_by_name("nloginpwd").send_keys(pwd)
    if driver.find_element_by_id("loginsubmit"):
        print('logining ...')
        driver.find_element_by_id("loginsubmit").click()
    time.sleep(1)
    tag = True
    while tag:
        driver.get("https://item.jd.com/3331229.html")
        if driver.find_element_by_link_text("加入购物车"):
            driver.find_element_by_link_text("加入购物车").click()
            tag = False
        time.sleep(1)
    if driver.find_element_by_link_text("去购物车结算"):
        driver.find_element_by_link_text("去购物车结算").click()
    if driver.find_element_by_link_text(".*去结算*."):
        driver.find_element_by_link_text(".*去结算*.").click()

    while True:
        try:
            driver.find_element_by_id('order-submit').click()
        except:
            time.sleep(0.1)
    now = datetime.datetime.now()
    print("success : ",now.strftime('%Y-%m-%d %H:%M:%S'))

login("1006652872","***********")
buy_on_time("2017-05-24 18:00:05")
