Project Title: ECM1400 Continuous Assessment COVID-19 Dashboard

INTRODUCTION
------------
Since the outbreak of COVID-19 the day-to-day routine for many people has been disrupted and keeping up-to-date with the local and national infection rates and news on government guidelineshas become a daily challenge.

Thanks to this COVID-19 dashboard you will be able to get up-to-date Covid infection rates coming directly from the Public Health England API and the top  UK headlines about covid coming directly from the the NEWSAPI website.


PREREQUISITES
------------
This project is intended to be run using Python 3.9.
All python scripts were developed using Microsoft Visual Studio Code.

PREREQUISITES/Modules
------------
In order to be able to use these features and get up-to-date data it was necessary to implement multiple modules including bu not limited to:
- The Flask module which was used to run the web application by implementing an interface using an HTML file which was already provided.

- The sched module which was used to let the user , on request, schedule updates to the user interface by updating the date at specified times.

- The uk_covid19 module which was used to get up-to-date case, death and hospitalisation data from Public Health Englandand 

- The requests module which is used to get up-to-date headlines data from NEWSAPI.

A complete list of modules imported can be found below (these modules will have to be install on the user's device in order to make the dashboard function correctly):

time /sched /csv /json /pandas /logging /requests / flask/ uk_covid19/ datetime
   
NOTE: You will see some other modules have been imported these are simply functions which are imported from other python scripts in the same folder.



PREREQUISITES/API
------------
In order to make the Dashboard work correctly you must have your own NEWSAPI api-key which you must input into the config.json file in the marked location.
To get your free api-key from NEWSAPI navigate to https://newsapi.org/ and follow the instructions provided on their website.

PREREQUISITES/File directories
------------
Please input the path to the config.json file, the covid_API_data.csv, the nation_2021-10-28.csv file in the marked locations in the following files : run.py / covid_news_handling.py / covid_data_handling.py / test_covid_data_handler.py

RUNNING DASHBOARD
------------
In order to run the dashboard make sure all files contained in the folder are contained within the working directory, make sure your API-key has been entered as instructed and that you have successfully run the run.py file. Once you have run the file navigate to 127.0.0.1:5000 in an internet browser in order to see the dashboard. You can now schedule your desired updates by selecting your choices in the scheduler section of the site, you will have the choice of the time of the update, what data should be updated and whether or not this update should be repeated.

NOTE: This dashboard was intended to be used by default to get COVID data for the city of EXETER (Devon/UK), to personalise the dashboard to represent your own city simply edit the appropriate value in the config.json file.
NOTE: The dashboard will automatically navigate to 127.0.0.1:5000/index after a certain time, this is normal and will not affect the use of the dashboard once redirected.


LOGGING INFO
------------
All logging information is saved in a file called logging_info.log file.
This information includes which functions have been called and what time and name has been inputed by the user into our scheduler.

NEWS ARTICLES:
------------
Up-to-date news articles are visible on the right hand side of the dashboard.
These news articles are uk news headlines about Covid with all headlines having to contain one of the following words: Covid COVID-19 coronavirus .

Note: Unfortunately I have not managed to correctly implement a feature to delete news articles at the request of the user, a version of the flask app where a news title can be deleted is available in extra.py but there are bugs with the deletion of news articles with only one news article title having the ability to be deleted at a time and the news article reappearing once the page is refreshed.
Any recommendation on how to fix this problem would be greatly appreciated.

DEVELOPPER INFORMATION:
------------
Matthew Lewis 
Contact Info : mjl233@exeter.ac.uk
Github : https://github.com/matthewlewis123