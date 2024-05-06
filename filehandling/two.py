
#read file (user.txt) and write into new file(emp.txt)

fp1 = open('user.txt','r')

data=fp1.read()
print(data) 

fp2 = open('emp.txt','w') 
fp2.write(data)
print("Writren successfully")
fp1.close()
fp2.close()
