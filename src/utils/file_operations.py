import json


def write_to_json(data, path):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


def read_from_json(path):
    with open(path, "r") as f:
        loaded_json = json.load(f)
    return loaded_json
