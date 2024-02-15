import requests
import os


def date_cui(cui):
    URL = f'https://api.openapi.ro/api/companies/{cui}'
    api_key = 'xgQEJPT3NbfzCskSrD2Wsihx8amcsYA5Pr8VAxMPc3Nny6c3Fg'
    headers = {'x-api-key': api_key}
    response = requests.get(URL, headers=headers, timeout=10)
    data = response.json()
    print(data)


date_cui(37659257)
