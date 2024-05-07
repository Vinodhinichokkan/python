import csv
fp=open('data.csv','r')
user_csv=csv.reader(fp)

print(type(user_csv))

users=list(user_csv)
print(type(users))
print(users)