import json

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

print(data['president']['name'])

with open('teste_json.json', 'w') as arq_json:
    json.dump(data, arq_json)
    
py_json = json.dumps(data)

print(py_json)
