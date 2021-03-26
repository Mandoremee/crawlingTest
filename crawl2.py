import time
import bs4
import pandas as pd
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions

##크롬드라이버가 설치된 절대경로를 설정해야 한다.
driver = webdriver.Chrome("E:\Chrome Download\chromedriver_win32\chromedriver.exe")
url = 'https://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&oid=001&isYeonhapFlash=Y'
driver.get(url)
time.sleep(3)

driver.find_element_by_xpath('//*[@id="search_option_button"]').click()
time.sleep(1)