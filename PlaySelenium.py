# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:58:47 2021

@author: AfifNF4
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

Path = "D:\chromedriver"
url = 'https://www.techwithtim.net/'

Dr = webdriver.Chrome(Path)
Dr.get(url)
search = Dr.find_element_by_name("s")
search.send_keys("Python")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(Dr, 20).until(EC.presence_of_element_located((By.ID,"main")))
    articles = main.find_elements_by_tag_name('article')
    
    for article in articles:
        p = article.find_element_by_class_name("entry-title")
        print(p.text)
    
except:
    print("try fail")

page_code = Dr.page_source
#print(page_code)

sleep(4)
Dr.quit()