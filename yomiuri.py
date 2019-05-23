import requests as rq
import time
import module
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

test_list = []

yomiuri_url = 'https://www.yomiuri.co.jp/national/'

driver = webdriver.Chrome('./chromedriver')
driver.get(yomiuri_url)
driver.maximize_window()

#click more btn
## you can change the number of clicks by for loops
for pageNum in range(1,3):
    print("clicked!")
    selected_selector = driver.find_element_by_xpath("//div[@class='c-more-btn']/a[@id='ajax_more_button']")
    actions = ActionChains(driver)
    actions.move_to_element(selected_selector).click().perform()

time.sleep(3)

#lists for datas
article_date = []
article_subject = []
article_data =[]

#save articles subjects
article_lists = driver.find_elements_by_class_name("c-list-title--default")
for i in article_lists:
    article_subject.append(i.text)

#get articles time
article_time = driver.find_elements_by_xpath("//div[@class='c-list-date']/time[@*]")
print(len(article_time))

for i in range(len(article_time)):
    article_date.append(article_time[i].get_attribute("datetime"))

#db connect
momentDB = module.mongoDBConnect()
japanCollection = momentDB.get_collection("Japan")

#db insert
for i in range(len(article_date)):
    post_jpn = {
        "writer": "yomiuri",
        "subject": article_subject[i],
        "time": article_date[i],
        "field": []
    }
    article_data.append(post_jpn)

print(article_data)

result = japanCollection.insert_many(article_data)
print(result.inserted_ids)
print("yomiuri db insert complete!")

