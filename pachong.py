# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 20:50:12 2021

@author: hp
"""
import requests
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm

# 模拟浏览器访问
Headers = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'

# 表头
csvHeaders = ['题号', '难度', '标题', '通过率', '通过数/总提交数']

# 题目数据
subjects = []

# 爬取题目
print('题目信息爬取中：\n')
for pages in tqdm(range(1, 11 + 1)):

    r = requests.get(f'http://www.51mxd.cn/problemset.php-page={pages}.htm', Headers)

    r.raise_for_status()

    r.encoding = 'utf-8'

    soup = BeautifulSoup(r.text, 'html.parser')

    td = soup.find_all('td')

    subject = []

    for t in td:
        if t.string is not None:
            subject.append(t.string)
            if len(subject) == 5:
                subjects.append(subject)
                subject = []

# 存放题目
with open('NYOJ_Subjects.csv', 'w', newline='') as file:
    fileWriter = csv.writer(file)
    fileWriter.writerow(csvHeaders)
    fileWriter.writerows(subjects)

print('\n题目信息爬取完成！！！')


