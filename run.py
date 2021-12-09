# These are the modules imported in order to make our code run
import time
import sched
import logging
from flask import Flask
from flask import request
from flask import render_template
from covid_news_handling import get_keys
from covid_data_handler import covid_API_request
from covid_data_handler import convert_API_data
from covid_data_handler import process_covid_csv_data
from covid_data_handler import parse_csv_data
from covid_data_handler import interval_definer
from covid_data_handler import schedule_covid_updates
from covid_news_handling import get_news
from covid_news_handling import update_news

#This defines our Flask app
app = Flask(__name__)  


#These lines are used to extract the API-Key and location information the user has stored in the config.json file and save it to respective variables.
keys = get_keys(r"<INSERT PATH TO config.json HERE>")
API_Key = keys['API_Key']
location = keys["location"]   
location_type= keys["location_type"]
nation = keys["nation"]

#These variables are used to store the user scheduled update information and the news articles resepctively.
updates = []
news_info = [] 

#These lines define what the url for our flask application will be.
@app.route("/")
@app.route("/index")
#This function puts all the necessary data for our dashboard in one place for it to be easily rendered into an HTML file.
def home(): 
    logging.basicConfig(level=logging.DEBUG,filename='logging_info.log', encoding='utf-8')
    covid_API_request()
    convert_API_data(covid_API_request())
    last7days_cases, current_hospital_cases, total_deaths = process_covid_csv_data(parse_csv_data(
        r"<INSERT PATH TO covid_API_data.csv HERE>"))
    covid_API_request(location= nation, location_type= "nation")
    convert_API_data(covid_API_request(location= nation, location_type= "nation"))
    national_last7days_cases, national_current_hospital_cases, national_total_deaths = process_covid_csv_data(parse_csv_data(
        r"<INSERT PATH TO covid_API_data.csv HERE>"))
    update_name = request.args.get("two")
    news_info = get_news()
    seen = set()
    news_articles = [] 
    for d in news_info:
        t = tuple(d.items())
        if t not in seen:
            seen.add(t)
            news_articles.append(d)
    if update_name:
        update_time = request.args.get("update")
        request_to_update_covid_data = request.args.get("covid-data")
        request_to_update_news = request.args.get("news")
        request_to_repeat_update = request.args.get("repeat")
        if update_time:
            updates.append({"title": update_name})
            updates.append({"content": update_time})
        else:
            updates.append({"title": "Error"})
            updates.append({"content": "Please select update time"})
        if request_to_repeat_update:
                if update_time:
                    update_interval = interval_definer(update_time= update_time)
                    if request_to_update_covid_data and request_to_update_news:
                        schedule_covid_updates(update_interval, update_name)
                        update_news(update_interval, update_name)
                        update_interval = interval_definer(update_time= update_time) + (24*3600)
                        schedule_covid_updates(update_interval, update_name)
                        update_news(update_interval, update_name)
                    elif request_to_update_covid_data and not request_to_update_news:
                        schedule_covid_updates(update_interval, update_name)
                        update_interval = interval_definer(update_time= update_time) + (24*3600)
                        schedule_covid_updates(update_interval, update_name)
                    elif request_to_update_news and not request_to_update_covid_data:
                        update_news(update_interval, update_name)
                        update_interval = interval_definer(update_time= update_time) + (24*3600)
                        update_news(update_interval, update_name)
                else:
                    logging.info("Update with name: " + update_name +": could not be set as required info (verify time was input) was not provided")
        else:
            if update_time:
                update_interval = interval_definer(update_time= update_time)
                if request_to_update_covid_data and request_to_update_news:
                    schedule_covid_updates(update_interval, update_name)
                    update_news(update_interval, update_name)
                elif request_to_update_covid_data and not request_to_update_news:
                    schedule_covid_updates(update_interval, update_name)
                elif request_to_update_news and not request_to_update_covid_data:
                    update_news(update_interval, update_name)
            else:
                 logging.info("Update with name: " + update_name +": could not be set as required info (verify time was input) was not provided")


    s0.run(blocking = False)
    s1.run(blocking= False)
    return render_template("index.html", news_articles = news_articles, updates = updates, location = location, local_7day_infections=last7days_cases, 
    nation_location = nation, hospital_cases = current_hospital_cases, deaths_total = total_deaths, national_7day_infections = national_last7days_cases)    


if __name__ == '__main__':
    #These lines define our schedulers
    s0 = sched.scheduler(time.time, time.sleep)
    s1 = sched.scheduler(time.time, time.sleep)
    #This line runs our Flask app
    app.run()  