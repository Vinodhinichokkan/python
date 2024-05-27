
import requests
from pymongo import MongoClient
import json 

resp=requests.get('https://jsonplaceholder.typicode.com/users')

user_list=resp.json()
""" user_json=json.loads(user_list)
print(type(user_json)) """

client=MongoClient('mongodb://localhost:27017/')
db=client['9am']
user_collection=db['users']

#user_collection.insert_one()
user_collection.insert_many(user_list)

print("Inserted successfully")
