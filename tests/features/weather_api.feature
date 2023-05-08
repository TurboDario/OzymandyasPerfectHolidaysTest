Feature: Weather API

  Background:
    Given the OpenWeatherMap API key

  Scenario Outline: Get weather data for a city
    Given I request the weather data for "<city>"
    When the response should have the city name "<city>"
    Then the response should have status code "200"

    Examples:
      | city     |
      | New York |
      | Málaga   |
      | Paris    |
      | Tokyo    |
      | Sydney   |
      | Madrid   |

  Scenario: Test API response for an invalid city
    Given I request the weather data for "InvalidCity"
    Then the response should have status code "404"

  Scenario Outline: Test API response time for a variable number of requests per second
    Given "<num_requests>" requests per second to the weather API for "London" should take less than "<seconds>" seconds

    Examples:
      | num_requests | seconds |
      # | 1000         | 90      |
      # | 100          | 30      |
      | 10           | 1       |