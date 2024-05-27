import requests

resp=requests.get('https://jsonplaceholder.typicode.com/users')
user_list=resp.json()

print(type(user_list))
data=[]
for user in user_list:
    data.append((user['id'],user['name'],user['email'],user['address']['city'],user['phone']))


print(data)km