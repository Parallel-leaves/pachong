# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 21:17:21 2021

@author: hp
"""
import requests
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm

# 模拟浏览器访问

Headers ={ 
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44'
}
#csv的表头
cqjtu_head=["日期","标题"]
#存放内容
cqjtu_infomation=[]


def get_time_and_title(page_num,Headers):#页数，请求头
    if page_num==66 :
        url='http://news.cqjtu.edu.cn/xxtz.htm'
    else :
        url=f'http://news.cqjtu.edu.cn/xxtz/{page_num}.htm'
    r=requests.get(url,headers=Headers)
    r.raise_for_status()
    r.encoding="utf-8"
    array={#根据class来选择
        'class':'time',
        }
    title_array={
     'target':'_blank'
    }
    page_array={
    'type':'text/javascript'
    }
    soup = BeautifulSoup(r.text, 'html.parser')
    time=soup.find_all('div',array)
    title=soup.find_all('a',title_array)
    temp=[]
    for i in range(0,len(time)):
        time_s=time[i].string
        time_s=time_s.strip('\n                                    ')
        time_s=time_s.strip('\n                                ')
        #清除空格
        temp.append(time_s)
        temp.append(title[i+1].string)
        cqjtu_infomation.append(temp)
        temp=[]

# 爬取题目
print('新闻信息爬取中：\n')
for pages in tqdm(range(66, 0,-1)):
    get_time_and_title(pages,Headers)

# 存放题目
with open('cqjtu_news.csv', 'w', newline='') as file:
    fileWriter = csv.writer(file)
    fileWriter.writerow(cqjtu_head)
    fileWriter.writerows(cqjtu_infomation)

print('\n新闻信息爬取完成！！！')


