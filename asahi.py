import requests as rq
import pymongo
from bs4 import BeautifulSoup
import module
import unicodedata

##mongo db connect
port = 27017;
conn = pymongo.MongoClient('168.131.30.129', port)
momentDB = conn.get_database("moment")
print("moment db loaded : ", momentDB)

japanCollection = momentDB.get_collection("Japan")
print("japan collection loaded : ", japanCollection)

##crawling
asahi_url = 'https://www.asahi.com/news/?iref=comtop_gnavi'
res = rq.get(asahi_url)
soup = BeautifulSoup(res.content, 'html.parser')

#lists for datas
article_date = []
article_subject = []
article_data =[]

#extract date
for tag in soup.select("a.SW"):
    for list in tag.select("span.Time"):
        returned_date = module.cutDate(list.text)
        article_date.append(returned_date)

for temp in soup.select("a.SW > span"):
    temp.decompose()

#extract article subjects
for category_ul in soup.find_all("ul", class_="List"):
    for link in soup.find_all("a", class_="SW"):
        normalized_subject = unicodedata.normalize("NFKD", link.text.strip())
        article_subject.append(normalized_subject)

#DB insert

for i in range(len(article_date)):
    post_jpn = {
        "writer": "asahi",
        "subject": article_subject[i],
        "time": article_date[i],
        "field": []
    }
    article_data.append(post_jpn)

print(article_data)

result = japanCollection.insert_many(article_data)
# print(result.inserted_ids)
print("db insert complete!")
