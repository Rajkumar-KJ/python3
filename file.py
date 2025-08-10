import json
import os

filename = 'data.json'

if not os.path.exists(filename):
    with open(filename, 'w') as f:
        json.dump([], f)

def read_data():
    with open(filename, 'r') as f:
        return json.load(f)

def write_data(data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def create_record(new_record):
    data = read_data()
    data.append(new_record)
    write_data(data)
    print("Record added.")

def read_records():
    data = read_data()
    for record in data:
        print(record)

def update_record(record_id, updated_data):
    data = read_data()
    for record in data:
        if record["id"] == record_id:
            record.update(updated_data)
            write_data(data)
            print("Record updated.")
            return
    print("Record not found.")

def delete_record(record_id):
    data = read_data()
    new_data = []

    for record in data:
        if record["id"] != record_id:
            new_data.append(record)

    if len(new_data) == len(data):
        print("Record not found.")
    else:
        write_data(new_data)
        print("Record deleted.")


# create_record({"id": 1, "name": "Alice", "age": 25})


print(read_data())
# update_record(1, {"age": 26})

print(os.getcwd())
# read_records()

# delete_record(1)

# read_records()
# print(os.listdir())
os.remove('data.json') 