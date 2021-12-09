# These are the modules imported in order to make our code run
import csv
import time
import sched
import pandas as pd
import logging
from uk_covid19 import Cov19API
from datetime import datetime
from time_conversions import hhmm_to_seconds
from covid_news_handling import get_keys

#This line sets up our logging functionality


#These two lines are used to extract the API-Key the user has stored in the config.json file and save it to a variable named API_Key
keys = get_keys(r"<INSERT PATH TO config.json HERE>")
API_Key = keys['API_Key']


#This function takes a csv file as an argument and returns a list of strings for the rows in the file.
def parse_csv_data(csv_filename : csv) -> list:
   logging.basicConfig(level=logging.DEBUG,filename='logging_info.log', encoding='utf-8')
   logging.info("The parse_csv_data function has been called")
   with open(csv_filename, "r") as file:
        data = csv.reader(file, delimiter = ",")
        covid_csv_data = []
        for row in data:
            covid_csv_data.append(row)
        return covid_csv_data
        

#This function takes a list of data as returned from the previous function and returns three variables; 
#the number of cases in the last 7 days, the current number of hospital cases and the cumulative number of deaths.
def process_covid_csv_data(covid_csv_data : list) -> tuple:
    logging.basicConfig(level=logging.DEBUG,filename='logging_info.log', encoding='utf-8')
    logging.info("The process_covid_csv_data function has been called")
    cumDailyNsoDeathsByDeathDate = []
    hospital_Cases = []
    newCasesBySpecimenDate = []
    for i in covid_csv_data:
        newCasesBySpecimenDate.append(i[6])
        hospital_Cases.append(i[5])
        cumDailyNsoDeathsByDeathDate.append(i[4])
    last7days_cases = (newCasesBySpecimenDate[3:10])
    last7days_cases = sum([int(float(i)) for i in last7days_cases])
    if hospital_Cases[1] != "NULL":
        current_hospital_cases = int(float(hospital_Cases[1])) 
    else:
        current_hospital_cases = "NULL"
    total_deaths = 0
    for i in cumDailyNsoDeathsByDeathDate:
        if i != "" and i !='cumDailyNsoDeathsByDeathDate':
            total_deaths += int(float(i))
            break
    return last7days_cases, current_hospital_cases, total_deaths

#In these variables we define the location, location type and nation which we want to receive Covid data from.
location = keys["location"]  
location_type= keys["location_type"]
nation = keys["nation"]

#This function takes two arguments called location and location type 
#with the default values of "Exeter" and "ltla" as these two variables have been previously defined as variables
#and returns up-to-date Covid data from the Public Health England COV19API as a dictionary. 
def covid_API_request(location :str = location , location_type :str= location_type) -> dict :
    logging.basicConfig(level=logging.DEBUG,filename='logging_info.log', encoding='utf-8')
    logging.info("The covid_API_request function has been called")
    location_data = ['areaType='+location_type, 'areaName='+location]
    cases_and_deaths = {
    "areaCode": "areaCode",
    "areaName": "areaName",
    "areaType": "areaType",
    "date": "date",
    "cumDailyNsoDeathsByDeathDate":"cumDeaths28DaysByPublishDate",
    "hospitalCases": "hospitalCases",
    "newCasesBySpecimenDate": "newCasesBySpecimenDate"}
    api = Cov19API(filters= location_data, structure=cases_and_deaths)
    data = api.get_json()
    return data



#As the data from the covid_API_request is returned as dictionary we must convert this data into a csv file
#in order to be able to process it using our previously defined process_covid_csv_data function.
def convert_API_data(input: dict) -> csv:
    logging.basicConfig(level=logging.DEBUG,filename='logging_info.log', encoding='utf-8')
    logging.info("The convert_API_data function has been called")
    df = pd.DataFrame.from_dict(input["data"])
    data= df.to_csv("covid_API_data.csv", na_rep='NULL', index = False)
    return "covid_API_data.csv"


#These two variables are used to get the current time and save it in the format HH:MM
a = datetime.now()
b= a.strftime("%H:%M")

#This function is used to get the difference in seconds between a time selected by the user and the current time.
def interval_definer(update_time :str = b) -> int:
    logging.basicConfig(level=logging.DEBUG,filename='logging_info.log', encoding='utf-8')
    logging.info("The interval_definer function has been called")
    current_time_in_s = hhmm_to_seconds(b)
    update_time_in_s = hhmm_to_seconds(str(update_time))
    if update_time_in_s >= current_time_in_s:
        update_interval = update_time_in_s - current_time_in_s
    elif update_time_in_s < current_time_in_s :
        update_interval = update_time_in_s - current_time_in_s + 24 * 3600
    return update_interval

#This line defines our s0 scheduler
s0 = sched.scheduler(time.time, time.sleep)

#This function is used to let the user schedule updates to the COVID-19 case, hospitalisation and deaths data.
def schedule_covid_updates(update_interval : int, update_name : str) -> None:
    logging.basicConfig(level=logging.DEBUG,filename='logging_info.log', encoding='utf-8')
    logging.info("The schedule_covid_updates function has been called")
    logging.info("The covid data update with name : " + update_name + ": is scheduled for in :"+ str(update_interval) + " seconds")
    e1 = s0.enter(update_interval, 1,covid_API_request)
    e2 = s0.enter(update_interval, 2, convert_API_data(covid_API_request()))



