#Factor Generator App

print("Welcome to Factor Generator App")

running = True
while running:
	get_input = int(input("Enter a number to determine all factors of that number : "))

	factor = []
	print(f'\nFactor of {get_input} are : ')
	for i in range(1,get_input+1):
		if get_input%i ==0:
			factor.append(i)
		
	for fact in factor:
		print(fact)
		
	#print a summary of the factors mathematically
	print("\nIn Summary : ")
	for i in range(int(len(factor)/2)):
		print(str(factor[i]) + '  *  ' + str(factor[-i-1]) + ' = ' + str(get_input))
	choice = input("\nRun again (Y/N) : ").lower()
	if choice != 'y':
		running = False
		print("Byeee")