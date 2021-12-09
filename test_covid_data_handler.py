#These are the modules imported in order to make our code run
from covid_data_handler import parse_csv_data
from covid_data_handler import process_covid_csv_data
from covid_data_handler import covid_API_request
from covid_data_handler import convert_API_data
from covid_data_handler import schedule_covid_updates

#These functions are designed to test the functions in our covid_data_handler.py file.

#This function tests our parse_csv_data function.
def test_parse_csv_data():
    data = parse_csv_data(r"<INSERT PATH TO nation_2021-10-28.csv HERE>")
    assert len(data) == 639

#This function tests our process_covid_csv_data function.
def test_process_covid_csv_data():
    last7days_cases , current_hospital_cases , total_deaths = \
        process_covid_csv_data ( parse_csv_data (r"<INSERT PATH TO nation_2021-10-28.csv HERE>") )
    assert last7days_cases == 240_299
    assert current_hospital_cases == 7_019
    assert total_deaths == 141_544

#This function tests our covid_API_request function.
def test_covid_API_request():
    data = covid_API_request()
    assert isinstance(data, dict)
    assert covid_API_request() == covid_API_request(location = "Exeter", location_type= "ltla")

#This function tests our convert_API_data function.
def test_convert_API_data():
    data = convert_API_data(covid_API_request())
    assert isinstance(data, str)

#This function tests our schedule_covid_updates function.
def test_schedule_covid_updates():
    schedule_covid_updates(update_interval=10, update_name='update test')

def run_all_data_tests():
    test_parse_csv_data()
    test_process_covid_csv_data()
    test_covid_API_request()
    test_convert_API_data()
    test_schedule_covid_updates()

#To run all tests at once uncomment the function below and run the script
#run_all_data_tests()