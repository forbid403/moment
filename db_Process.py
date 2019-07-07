import pymongo
import re
import os
import urllib.request
port = 27017;

def mongoDBConnect():
    conn = pymongo.MongoClient('168.131.30.129', port)
    momentDB = conn.get_database("moment")
    print("moment db loaded : ", momentDB)
    return momentDB

def loadArticles():
    jpCollection = mongoDBConnect().Japan
    cursor = jpCollection.find()
    article_List = []
    for subject in cursor:
        article_List.append(subject["subject"])

    removeSpace(article_List)
    return article_List

def removeSpace(articles):
    for article in articles:
        re.sub(r'(?<=(?![A-Za-z])[^\W\d_])\s+(?=(?![A-Za-z])[^\W\d_])', '', article)



def download_Stopwords(path):
    url = 'http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt'
    if os.path.exists(path):
        print('File already exists.')
    else:
        print('Downloading...')
        urllib.request.urlretrieve(url, path)

def create_stopwords(file_path):
    stop_words = []
    for w in open(path, "r"):
        w = w.replace('\n', '')
        if len(w) > 0:
            stop_words.append(w)
    return stop_words

path = "stop_words.txt"
download_Stopwords(path)
