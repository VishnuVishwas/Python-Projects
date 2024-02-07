# Request API

import requests
import json

# request from external source
responce = requests.get("https://jsonplaceholder.typicode.com/todos/1")
if responce.status_code == 200:
    data = responce.json()
    title = data['title']
    completed = data['completed']
    print(f"Title: {title}, Completed: {completed}")
else:
    print("Not found.")

# request from internal json file
with open('weather_data.json', 'r') as file:
    data = json.load(file)
    city = data['city']
    temparature = data['temparature']
    print(f"City: {city}\nTemparature: {temparature}")
