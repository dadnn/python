import requests

api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
x = response.json()
stat = response.status_code

print(x)
print("Hold up...")

todo = {"userId": 1, "title": "Wash car", "completed": False}
response = requests.put(api_url, json=todo)
y = response.json()

print(y)