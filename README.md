# Project Name

This project tests the OpenWeatherMap API using Python and Behave.

## Prerequisites

- Python 3.x
- pip

## Setup

1. Clone the repository.
2. Create a virtual environment:
```
python3 -m venv venv
```
3. Activate the virtual environment:
- On Linux/macOS:
  ```
  source venv/bin/activate
  ```
- On Windows:
  ```
  venv\Scripts\activate
  ```
4. Install the required packages:
```
pip install -r requirements.txt
```
5. Enter your API key
Enter your API key in the config.json file.

## Running Tests

To run the Behave tests, execute the following command in the project's root directory:
```
behave tests/features
```
