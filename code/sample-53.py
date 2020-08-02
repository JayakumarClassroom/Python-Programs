#Dictionary - Database Admin Program


print("Welcome to Database Admin Program")

#username and password database
user_db = {	'admin' : 'admin12345', 'jay' : 'jay1234567', 'sam' : 'sam1234567', 'mike' : 'mike1234567'}

#Get the username as input
get_username = input("Enter Your Username : ").lower()

#check the username in database
if get_username in user_db.keys():
	get_password = input("Enter Your Password : ").lower()
	if user_db[get_username] == get_password:
		print(f'\nHello {get_username}! You are logged in')	
		#printing all the user detail for ADMIN LOGIN
		if get_username == 'admin':
			print("\nHere is the current user database:")
			for key, val in user_db.items():
				print(f"\tUsername: {key}   \tPassword: {val}")
					
		#for other users				
		else:
			change_pass = input("would you like to change password ? (Y/N)").lower()
			if change_pass == 'y':
				change_password = input("What would you like you new password to be : ")
				len_new_password = len(change_password)
				if len_new_password > 8:
					user_db[get_username]=change_password
					print(f'\n{get_username} your new password is {user_db[get_username]}')
				else:
					print("Password must be minimum of 8 character")
					print(f'\n{get_username} your old password is {user_db[get_username]}')
				
			else:
				print("You didn't change your password")
				print(f'\n{get_username} your old password is {user_db[get_username]}')
		
	else: 
		print(f"Your password is invalid for the {get_username}")	
else:
	print("Username not in database. Goodbye!!!!")
