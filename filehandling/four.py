#append text into emp.txt file 

fp=open('emp.txt','a')
data = "Good Night"
fp.write(data)
fp.close()