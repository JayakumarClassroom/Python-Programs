#Nested Dictionary

friends_list = {
	'jay':['sam','mike','john'],
	'steve':['billy','robin','sharma'],
	'jobs': ['mark','anto','kumar']
}

for k,v in friends_list.items():
	print(f"{k}'s friends are")
	for vals in v:
		print(f'\t{vals}')


#printing username and details
user_directory = {
	'iamjayakumars':{
			'fname':'Jayakumar',
			'lname':'Sadhasivam',
			'country':'India',
			'color':'Black'
		},
	'steve':{
		'fname':'Steve',
		'lname':'Jobs',
		'country':'USA',
		'color':'Blue'
	}
}

for key, value in user_directory.items():
		print(f"\nUsername: {key}")
		for item,info in value.items():
			print(f'{item} : {info}')			