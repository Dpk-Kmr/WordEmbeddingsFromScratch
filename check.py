from preprocessing import load_data

text_lines = load_data.load_csv_file('data.csv')
import json

# Parsing JSON
json_string = '{"name": "Alice", "age": 30, "city": "New York"}'
data = json.loads(json_string)
print(data["name"])  # Output: Alice

# Generating JSON
data = {
    "name": "Bob",
    "age": 25,
    "city": "Los Angeles"
}
print(data)
json_string = json.dumps(data, indent=4)
print(type(json_string))
print(json_string)