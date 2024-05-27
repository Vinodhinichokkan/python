import requests

resp=requests.get('https://dummyjson.com/products')
product_data=resp.json()


products=product_data['products']

groceries=[]
for product in products:
    if product['category']=='groceries':
        groceries.append(product)

try:
    client=MongoClient('mongodb://localhost:27017/')
    db=client['10AM']
    col=db['products']
    col.insert_many(groceries)
    print('Data inserted successfully')

except:
    

