import json

json_data = '{"nimi":"Darja Suhhanova","age":18,"on_prillid":true}'

data_ = json.loads(json_data)

for id_, data in enumerate(data_):
    print(id_, ": ", data)

for key, value in data_.items():
    print(key, value)
print(data_)