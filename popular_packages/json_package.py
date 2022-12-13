import json

dict_data = {
    "name": "Carlos",
    "lastname": "Sanjuan",
    "email": "carlosdsanjuan@outlook.com"
}

dict_json = json.dumps(dict_data)

print(dict_json)