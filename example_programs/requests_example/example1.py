import json
import requests


url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

print(response.status_code)

with open("response.json","w") as file:
    json.dump(response.json(), file, indent=4)
