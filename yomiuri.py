import requests as rq
import time
from bs4 import BeautifulSoup
from selenium import webdriver
test_list = []

#요미우리는 국내 뉴스 크롤링
yomiuri_url = 'https://www.yomiuri.co.jp/national/'

driver = webdriver.Chrome('./chromedriver')
driver.get(yomiuri_url)
driver.maximize_window()
driver.implicitly_wait(3)

for pageNum in range(1,3):
    selected_selector = driver.find_element_by_id("ajax_more_button").click()
    time.sleep(0.5)

article_lists = driver.find_elements_by_class_name("c-list-title--default")
for i in article_lists:
    print(i.text)