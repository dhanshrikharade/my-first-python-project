import json
from urllib.request import urlopen

url = "https://jsonplaceholder.typicode.com/todos/1"

with urlopen(url) as response:
    data = json.load(response)

print("Todo:")
print("Title:", data["title"])
print("Completed:", data["completed"])