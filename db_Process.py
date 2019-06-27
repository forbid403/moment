import pymongo
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
    return article_List

