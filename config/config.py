import json


def __get_attributes_from_json(attribute):
    with open("config.json", "r") as f:
        data = json.load(f)
    return data[attribute]


address = __get_attributes_from_json("address")
client_id = __get_attributes_from_json("client_id")
client_secret = __get_attributes_from_json("client_secret")
