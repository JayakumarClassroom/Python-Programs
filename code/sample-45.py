#Condition statement  - Shipping Account Program

print("Welcome to Shipping Account Program")

#predefined username
unames=['jay','mike','sam','kumar','swamy','sri',"jessi",'allen','tom','jerry']

username = input("Hello! What is your username : ").lower().strip()
if username in unames:
	print(f"\nWelcome {username} !!!")
	print("\n\tShipping Order from 0 to 100 : \t\t Rs 100.00 each")
	print("\tShipping Order from 101 to 500 : \t Rs 85.00 each")
	print("\tShipping Order from 501 to 1000 : \t Rs 75.00 each")
	print("\tShipping Order from over 1000 : \t Rs 50.00 each")

	order = int(input("\nHow many items do you like to ship : "))

	#Payment calculation - using condition statement.

	if order > 0 and order <= 100: 
		money= order * 100
		print(f'\nTo ship {order} items, it will cost you Rs {money} at RS 100.00 per item.')
	elif order > 100 and order <= 500: 
		money= order * 85
		print(f'\nTo ship {order} items, it will cost you Rs {money} at RS 85.00 per item.')
	elif order > 500 and order <= 1000: 
		money= order * 75
		print(f'\nTo ship {order} items, it will cost you Rs {money} at RS 75.00 per item.')
	elif order >= 1000:
		money= order * 50
		print(f'\nTo ship {order} items, it will cost you Rs {money} at RS 50.00 per item.')
	
	
	#order the item
	order_item = input("\nWould you like to place the order (Y/N) : ").lower()
	if order_item.startswith('y'):
		print(f'\nOkay. Shipping your {order} items.\nThank You !!!! ')
	else:
		print("Order Not Place :( ")
		
else:
	print("Sorry! You don't have an account with our company.\nThanks for visiting")