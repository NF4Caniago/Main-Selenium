# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 17:17:46 2021

@author: AfifNF4
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

Path =  "D:\chromedriver"
url = 'https://www.techwithtim.net/'

driver = webdriver.Chrome(Path)
driver.get(url)

link = driver.find_element_by_link_text("Python Programming")
link.click()

try:
    link2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT,"Beginner Python Tutorials")))
    link2.click()
    
    link2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"sow-button-19310003")))
    link2.click()
    
    driver.back()
    driver.back()
    driver.back()
    driver.forward()
    driver.forward()
    
except:
    print("try fail")

sleep(5)
driver.quit()