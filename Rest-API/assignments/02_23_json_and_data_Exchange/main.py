import json

# JSON string to be parsed
json_string_to_parse = '{"product": "Phone", "price": 599.99, "quantity": 10}'

# Parse JSON
parsed_data = json.loads(json_string_to_parse)

# Accessing values
print("Product:", parsed_data['product'])
print("Price:", parsed_data['price'])
print("Quantity:", parsed_data['quantity'])

# Python dictionary to be converted to JSON
python_dict_to_convert = {"product": "Tablet", "price": 349.99, "quantity": 5}

# Convert to JSON
json_data_to_generate = json.dumps(python_dict_to_convert, indent=2)

# Output generated JSON string
print("\nGenerated JSON:")
print(json_data_to_generate)
