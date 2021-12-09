#These are the modules imported in order to make our code run
import requests    
import json
import time
import sched
import logging

#This line sets up our logging functionality


#This function is used to be able to extract dictionary values from a json file.
def get_keys(path : json) -> dict:
    logging.basicConfig(level=logging.DEBUG,filename='logging_info.log', encoding='utf-8')
    logging.info("The get_keys function has been called")
    with open(path) as f:
        return json.load(f)

#These two lines are used to extract the API-Key the user has stored in the config.json file and save it to a variable named API_Key
keys = get_keys(r"<INSERT PATH TO config.json HERE>")
API_Key = keys['API_Key']

#This function is used to get up-to-date news headlines from NEWSAPI.
def news_API_request(covid_terms : str = 'Covid COVID-19 coronavirus') -> tuple:
    logging.basicConfig(level=logging.DEBUG,filename='logging_info.log', encoding='utf-8')
    logging.info("The news_API_request function has been called")
    base_url = "https://newsapi.org/v2/top-headlines?"
    api_key = API_Key
    country = "gb"
    complete_url = base_url  + "country=" + country + "&apiKey=" + api_key
    response = requests.get(complete_url)
    b = response.json()
    articles = b["articles"]
    a = covid_terms.split(" ")   
    return articles, a     


 
news_info = [] #This list stores the news articles about Covid.

#This function is used to filter the NEWSAPI top headlines so that only articles about covid are kept and then append these articles to our news_info variable.
def add_news_article(api_data : tuple = news_API_request()) -> None:
    logging.basicConfig(level=logging.DEBUG,filename='logging_info.log', encoding='utf-8')
    logging.info("The add_news_article function has been called")
    articles, a = api_data
    for news in articles:
        for i in range(len(a)):
            if a[i] in news["title"] and news["title"] not in news_info:
                news_info.append({"title": news["title"]})
                news_info.append({"content": news["content"]})


#This function is used to run our previous function and save our top headlines about covid to our news_info variable.
def get_news() -> list:
    logging.basicConfig(level=logging.DEBUG,filename='logging_info.log', encoding='utf-8')
    logging.info("The get_news function has been called")
    add_news_article()
    return news_info    

#This line defines our s1 scheduler
s1 = sched.scheduler(time.time, time.sleep)

#This function is used to let the user schedule updates to the Covid headlines.
def update_news(update_interval : int , update_name : str) -> None:
    logging.basicConfig(level=logging.DEBUG,filename='logging_info.log', encoding='utf-8')
    logging.info("The update_news function has been called")
    logging.info("The news update with name : " + update_name + ": is scheduled for in :"+ str(update_interval) + " seconds")
    e2 = s1.enter(update_interval, 1, get_news)
    
