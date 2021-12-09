#These are the modules imported in order to make our code run
from covid_news_handling import news_API_request
from covid_news_handling import add_news_article
from covid_news_handling import get_news
from covid_news_handling import update_news

#These functions are designed to test the functions in our covid_news_handling.py file.

#This function tests our news_API_request function.
def test_news_API_request():
    assert news_API_request()
    assert news_API_request('Covid COVID-19 coronavirus') == news_API_request()

#This function tests our add_news_articles function.
def test_add_news_article():
    assert add_news_article(api_data= news_API_request())== add_news_article()

#This function tests our get_news function.
def test_get_news():
    data = get_news()
    assert isinstance(data, list)

#This function tests our update_news function.
def test_update_news():
    update_news(3600, 'test')

#To run all tests at once uncomment the function below and run the script
def run_all_news_tests():
    test_news_API_request()
    test_add_news_article()
    test_get_news()
    test_update_news()

#To run all tests at once uncomment the function below and run the script
#run_all_news_tests()