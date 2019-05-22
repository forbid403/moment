import requests as rq
import pymongo
from pymongo import MongoClient
from bs4 import BeautifulSoup
import module

##mongo db connect
port = 27017;
conn = pymongo.MongoClient('localhost', port)
momentDB = conn.get_database("moment")
print("moment db loaded : ", momentDB)

japanCollection = momentDB.get_collection("japan")
print("japan collection loaded : ", japanCollection)

##crawling
asahi_url = 'https://www.asahi.com/news/?iref=comtop_gnavi'

res = rq.get(asahi_url)
soup = BeautifulSoup(res.content, 'html.parser')

for tag in soup.select("a.SW"):
    for list in tag.select("span.Time"):
        print(list.text)

for temp in soup.select("a.SW > span"):
    temp.decompose()

news = soup.select("a.SW > span")
for new in news:
    print(new.text.strip())

#날짜랑 기사 제목 따로 DB 저장하기

client = MongoClient('localhost', 27017)
db = client["moment"]
collection = db["Japan"]

post_jpn = {
    "writer" : "writer",
    "subject" : "subject",
    "time" : "",
    "field" : []
}

returned_date = module.cutDate()
print(returned_date)
#collection.insert(post_jpn)

