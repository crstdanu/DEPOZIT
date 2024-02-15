import requests


cui = '15412450'
URL = f'https://api.openapi.ro/api/companies/{cui}'
API_KEY = 'ei7offEoVS72Gjs6cwSGTzuynipv9vX8cTkUwbs22scSCjjj8Q'
headers = {'x-api-key': API_KEY}
response = requests.get(URL, headers=headers, timeout=10)

data = response.json()
print(data)

with open('data_cui_2.txt', 'w') as f:
    f.write(str(data))
