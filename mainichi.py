import requests as rq
from bs4 import BeautifulSoup

#마이니치는 속보를 크롤링함
mainichi_url = 'https://mainichi.jp/flash'
page_path = '/%d'
page = 1

while True:
    sub_path = page_path%(page)
    page += 1
    print("page : " + sub_path);
    res = rq.get(mainichi_url + sub_path)
    if(res.status_code != 200):
        break
    soup = BeautifulSoup(res.content, 'lxml')
    for category_ul in soup.find_all("ul", class_="list-typeA typeA-date"):
        for link in soup.find_all("span", class_="midashi"):
            print(link.text)