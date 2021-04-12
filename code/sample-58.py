#While Loop - Even Odd Sorter App

print("Welcome to Even Odd Sorter App ")
running = True
while running:
	user_data = input("\nEnter in a string of numbers seperated by a comma (,) : ")
	user_data = user_data.replace(' ','')
	user_split_data = user_data.split(',')
	print(user_split_data)

	even = []
	odd = []
	
	#RESULT Summary 
	print("\nResult Summary ..................")

	for i in user_split_data:
		i = int(i)
		if i % 2==0:
			even.append(i)
			print(f'{i} is Even!')
		else:
			odd.append(i)
			print(f'{i} is Odd!')
	
	#sorting the numbers
	even.sort()
	odd.sort()
	
	#printing the even numbers alone
	print(f'\nThe following "{len(even)}" Even Numbers are : ')
	for i in even:
		print(f'\t{i}')
		
	#printing the odd numbers alone
	print(f'\nThe following "{len(odd)}" ODD Numbers are : ')
	for i in odd:
		print(f'\t{i}')
	
	#Play again or not 
	choice = input("Do you want to play again??? (y/n) : ")
	if choice != 'y':
		running=False

print("Thanks you!!!!")