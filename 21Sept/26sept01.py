import json

with open('test.json', 'r') as json_file:

    data = json.load(json_file)

print(data)

