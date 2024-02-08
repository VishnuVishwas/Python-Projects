# parsing json data

import json 

json_data = '{"name": "John", "age": 30, "city": "New York"}'
pasred_data = json.loads(json_data)

print("Parsed Data: ")
print(pasred_data['name'])
print(pasred_data['age'])
print(pasred_data['city'])

# Generating JSON Data
data = {"name": "Jane", "age": 25, "city": "San Francisco"}
json_data = json.dumps(data, indent=2)
print("\nJSON Data: ")
print(json_data)

