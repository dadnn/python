import requests
import json
import time

api_url = "https://pokeapi.co/api/v2/pokemon/pikachu"
response = requests.get(api_url)
x = response.json()

# Returned full JSON, timer, then returned only name value
# print(x)
print("Hold up...")
time.sleep(2)
print("The name is " + x["forms"][0]["name"])


