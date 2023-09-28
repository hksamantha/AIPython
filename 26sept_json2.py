import json

data = {'name': 'Dasun Athukorala', 'age': 20, 'city': 'Colombo'}

with open('test.json', 'w') as json_file:

    json_data = json.dumps(data) #convert Dictionary to json format

    json_file.write(json_data)





