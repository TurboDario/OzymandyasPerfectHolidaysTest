from behave import given, when, then, step
from weather_api.config import load_config
from weather_api.weather import get_weather_data
import time

config = load_config()

@step('the OpenWeatherMap API key')
def step_given_api_key(context):
    context.api_key = config["api_key"]

@step('I request the weather data for "{city}"')
def step_request_weather_data(context, city):
    try:
        context.weather_data = get_weather_data(city, context.api_key)
    except Exception as e:
        assert False, f"Error requesting weather data for {city}: {str(e)}"

@step('the response should have the city name "{city}"')
def step_check_city_name(context, city):
    try:
        assert context.weather_data["name"] == city, f"Expected city name {city}, but got: {context.weather_data['name']}"
    except KeyError:
        assert False, "City name not found in the response"

@step('The response should have status code "{status_code:d}"')
def step_check_status_code(context, status_code):
    status_code = str(status_code)
    weather_code = str(context.weather_data["cod"])
    assert weather_code == status_code, f"Expected status code {status_code}, but got: {context.weather_data['cod']}"

@step('"{num_requests}" requests per second to the weather API for "{city}" should take less than "{seconds}" seconds')
def step_send_requests_per_second(context, num_requests, city, seconds):
    num_requests = int(num_requests)
    acceptable_response_time = float(seconds)
    start_time = time.time()

    try:
        for _ in range(num_requests):
            context.weather_data = get_weather_data(city, context.api_key)
    except Exception as e:
        assert False, f"Error sending requests: {str(e)}"

    context.response_time = time.time() - start_time
    assert context.response_time < acceptable_response_time, f"Response time too slow: {context.response_time} seconds"
