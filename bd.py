# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 20:28:00 2021

@author: hp
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
#进入网页
driver.get("https://www.baidu.com/")

p_input = driver.find_element_by_id("kw")
p_input.send_keys('知乎')
#点击搜索按钮
p_btn=driver.find_element_by_id('su')
p_btn.click()