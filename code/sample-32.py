#Write a Python program to count the number of 4 in a given list. 

get_input=int(input("Enter the number in a list : "))
l=[]
count=0
for i in range(1,get_input+1):
	l.append(int(input("Enter the value : ")))
for x in l:
	if x == 4:
		count+=1
print("Total number of 4 is ", count)