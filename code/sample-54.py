#Dictionary - Polling APP 


print("Welcome to Polling App")

get_issue = input("\nWhat is the Yes or No issue you will be voting on today : ")

vote_time = int(input("What is the number of votes you will be allow on this issue : "))
password = input("Enter a password to start the polling : ")

#intialize variables
yes=0
no=0
voting={}

#simulate voting
for i in range(vote_time):
	full_name = input("\nEnter your Full Name : ").title().strip()
	if full_name in voting.keys():
		print("Sorry, It seems your already voted.")
	else:
		print("Here is our issue :" + get_issue)
		choice = input("What do you think ..... Yes or No ??").lower()
		if choice == "yes" or choice == 'y':
			choice = 'yes'
			yes += 1
		elif choice == "no" or choice == 'n':
			choice = 'no'
			no += 1
		else:
			print('That is not a YES or No vote.')
		
		#Add vote to dictionary
		voting[full_name]=choice
		print(f'Thank you {full_name}! Your vote has been recorded')
		
#show who actually voted
total_votes = len(voting.keys())
print(f"\nThe following {total_votes} people voted : ")
for key in voting.keys():
	print(key)

#summarize the voting results
print(f"\nOn the following issues: {get_issue}")
if yes > no:
	print("YES Wins!!!!! "+ str(yes) + " votes to " + str(no) + ".")
elif no > yes:
	print("NO Wins!!!!! "+ str(no) + " votes to " + str(yes) + ".")
else:
	print("It was a tie!!!!! " + str(no) + " votes to " + str(yes) + ".")

guess = input("\nTo see the voting results enter the admin password : ")
if guess == password:
	for k,v in voting.items():
		print(f'Voter {k}   \tVote: {v} value')
else:
	print("sorry, that is not the correct passowrd")