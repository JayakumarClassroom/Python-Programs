#Conditional Loop - VOTER Registration APP

print("Welcome to VOTER Registration APP")

name=input("Enter you Name : ").title().strip()
age=int(input("Enter your Age : "))

#Check whether the user age is greater than 18 or not
if (age >= 18):
	print(f'\nCongratulations {name}! You are old enough to register the vote.')
	
	#list of political parties
	party_list=['Republican','Democratic','Independent','Green']
	
	print('\nHere is a list of political parties to join')
	for items in party_list:
		print(f"\t-{items}")
	
	#Choosing the party
	party = input("What party would you like to join : ").title().strip()
	
	if party in party_list:
		print(f'Congratulations {name}! You have joined in the {party} Party!')
		if party=='Republican' or party=='Democratic':
			print("Thats a major party")
		elif party=='Independent':
			print("Your an Independent Person")
		else:
			print("That is not a major party")
	else:
		print("Thats not a party")
else:
	print("Your not old enough to Register your VOTE")
	
	

#
#elif party.startswith('D'):
#		print(f'Congratulations {name}! You have joined in the Democratic Party! \nThats a second major party.')
#	elif party.startswith('I'):
#		print(f'Congratulations {name}! You have joined in the Independent Party! \nThats a not major party.')
#	elif party.startswith('G'):
#			print(f'Congratulations {name}! You have joined in the Gree Party! \nNothing to say about this party.')
#	