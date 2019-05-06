import requests as rq
from bs4 import BeautifulSoup

asahi_url = 'https://www.asahi.com/news/?iref=comtop_gnavi'

res = rq.get(asahi_url)
soup = BeautifulSoup(res.content, 'html.parser')

for category_ul in soup.find_all("ul", class_="List"):
    for link in soup.find_all("a", class_="SW"):
        print(link.text)

