import json 
#что бы использовать джисон нужно преобразовать его в дикшинари 

#пример джиосна 

json_sample = '''{
    "students": [
        {
            "id": 1,
            "name": "Tim",
            "age": 21,
            "full-time": true
        },
        {
            "id": 2,
            "name": "Joe",
            "age": 33,
            "full-time": false
        }
    ]
}
'''

data = json.loads(json_sample) #load to string json -> dic
print(data)
data['test'] = True

new_json = json.dumps(data, indent = 4) #это обратно с дикшинори в джисон
print(new_json)
