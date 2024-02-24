import requests
import pprint

URL = "http://127.0.0.1:8000/drf/furnizori/"

response = requests.get(URL)

pprint.pprint(response.json())
