#import time
#import bs4
#import pandas as pd
#import pyautogui
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.common import exceptions

##크롬드라이버가 설치된 절대경로를 설정해야 한다.
#driver = webdriver.Chrome("E:\Chrome Download\chromedriver_win32\chromedriver.exe")
#url = 'https://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&oid=001&isYeonhapFlash=Y'
#driver.get(url)
#time.sleep(3)

#driver.find_element_by_xpath('//*[@id="search_option_button"]').click()
#time.sleep(1)
#----------------------------------------------김경민 하다가 막힘...
#참고하던 블로그 주소 :: https://blog.naver.com/tjddud9353/222267414901


#탄성호 코드 사용--->경민 ver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import time

#######
options = webdriver.ChromeOptions()
#options.add_argument('headless')

ua = UserAgent(verify_ssl=False)
userAgent = ua.random

options = Options()
options.add_argument(f'user-agent={userAgent}')
driver = webdriver.Chrome(options=options, executable_path=r'E:\Chrome Download\chromedriver_win32\chromedriver.exe')
###### 봇탐지 우회


# 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
driver.implicitly_wait(3)
time.sleep(3)

#연합뉴스 속보 페이지
url = "https://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y"

driver.get(url)
#연합뉴스 속보 페이지의 content 스크래핑
Root = driver.find_element_by_class_name("content").text
print(Root)