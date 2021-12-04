# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 21:24:38 2021

@author: hp
"""


from selenium import webdriver
import time
import csv
from tqdm import tqdm#在电脑终端上显示进度，使代码可视化进度加快
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
#加载页面
driver.get("https://www.jd.com/")
time.sleep(3)

#定义存放图书信息的列表
goods_info_list=[]
#爬取200本
goods_num=200
#定义表头
goods_head=['价格','名字','链接']
#csv文件的路径和名字
goods_path='C:\\Users\\28205\\Documents\\Tencent Files\\2820535964\\FileRecv\\qinming.csv'

#向输入框里输入Java
p_input = driver.find_element_by_id("key")
p_input.send_keys('法医秦明')

#button好像不能根据类名直接获取，先获取大的div，再获取按钮
from_filed=driver.find_element_by_class_name('form')
s_btn=from_filed.find_element_by_tag_name('button')
s_btn.click()#实现点击

#获取商品价格、名称、链接
def get_prince_and_name(goods):
    #直接用css定位元素
    #获取价格
    goods_price=goods.find_element_by_css_selector('div.p-price')
    #获取元素
    goods_name=goods.find_element_by_css_selector('div.p-name')
    #获取链接
    goods_herf=goods.find_element_by_css_selector('div.p-img>a').get_property('href')
    return goods_price,goods_name,goods_herf

def  drop_down(web_driver):
    #将滚动条调整至页面底部
    web_driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(3)

#获取爬取一页
def crawl_a_page(web_driver,goods_num):
    #获取图书列表
    drop_down(web_driver)
    goods_list=web_driver.find_elements_by_css_selector('div#J_goodsList>ul>li')
    #获取一个图书的价格、名字、链接
    for i in tqdm(range(len(goods_list))):
        goods_num-=1
        goods_price,goods_name,goods_herf=get_prince_and_name(goods_list[i])
        goods=[]
        goods.append(goods_price.text)
        goods.append(goods_name.text)
        goods.append(goods_herf)
        goods_info_list.append(goods)
        if goods_num==0:
            break
    return goods_num

while goods_num!=0:
    goods_num=crawl_a_page(driver,goods_num)
    btn=driver.find_element_by_class_name('pn-next').click()
    time.sleep(1)
write_csv(goods_head,goods_info_list,goods_path)
