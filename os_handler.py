import json

json_file_path = './task.json'

def load_json(file_path):
    """Load the data from the file"""
    with open(file_path, 'r') as file:
        return json.load(file)

def dump_json(file_path, new_data):
    """Insert new data from load file function"""
    with open(file_path, 'w') as file:
        json.dump(new_data, file, indent=4)

