# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 20:52:08 2021

@author: hp
"""


#from bs4 import BeautifulSoup as bs
from selenium import webdriver
import csv
#from selenium.webdriver.chrome.options import Options
from tqdm import tqdm#在电脑终端上显示进度，使代码可视化进度加快
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://quotes.toscrape.com/js/')
#定义csv表头
quote_head=['名言','作者']
#csv文件的路径和名字
quote_path='C:\\Users\\28205\\Documents\\Tencent Files\\2820535964\\FileRecv\\quote_csv.csv'
#存放内容的列表
quote_content=[]

'''
function_name:write_csv
parameters:   csv_head,csv_content,csv_path
csv_head:     the csv file head
csv_content:  the csv file content,the number of columns equal to length of csv_head
csv_path:     the csv file route
'''
def write_csv(csv_head,csv_content,csv_path):
    with open(csv_path, 'w', newline='') as file:
        fileWriter =csv.writer(file)
        fileWriter.writerow(csv_head)
        fileWriter.writerows(csv_content)
        print('爬取信息成功')

###
#可以用find_elements_by_class_name获取所有含这个元素的集合（列表也有可能）
#然后把这个提取出来之后再用继续提取
quote=driver.find_elements_by_class_name("quote")
#将要收集的信息放在quote_content里
for i in tqdm(range(len(quote))):   
    quote_text=quote[i].find_element_by_class_name("text")
    quote_author=quote[i].find_element_by_class_name("author")
    temp=[]
    temp.append(quote_text.text)
    temp.append(quote_author.text)
    quote_content.append(temp)
write_csv(quote_head,quote_content,quote_path)
