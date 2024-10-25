import json

json_file_path = './task.json'

def load_json(file_path):
    """Load the data from the file"""
    with open(file_path, 'r') as file:
        return json.load(file)

def increment_id_number():
    data = load_json(json_file_path)
    id_number = data.get("amounts_of_list", 0) + 1
    data["amounts_of_list"] = id_number

    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)

    return id_number

def dump_json(file_path, new_data):
    """Insert new data from load file function"""
    with open(file_path, 'w') as file:
        json.dump(new_data, file, indent=4)

def load(task: str):
    data = load_json(json_file_path)
    data["list_of_task"].append(task)
    dump_json(json_file_path, data)
