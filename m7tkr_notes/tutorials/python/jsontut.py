import json
from urllib.request import urlopen

with urlopen('https://jsonplaceholder.typicode.com/posts') as f:
    source = f.read()

data = json.loads(source)  # loads json string into python object

print(json.dumps(data, indent=2))  # dumps python object into json string

with open('./filedir/new_posts.json', 'w') as f:
    json.dump(data, f, indent=2)
