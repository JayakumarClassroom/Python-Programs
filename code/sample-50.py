#Nesting Dictionary

user_0={
	'name':'Jay',
	'age':32
}
user_1={
	'name':'Sam',
	'age':16
}
user_2={
	'name':'Mike',
	'age':55
}
user_list = [user_0,user_1,user_2]
for details in user_list:
	for k,v in details.items():
		print(k,v)
	print("\n")


#creating empty list

data=[]
for data_val in range(50):
	new_users = {'username':'NA','password':'pass123'}
	data.append(new_users)

#printing the first 10 values
for i in data[:10]:
	print(i)

