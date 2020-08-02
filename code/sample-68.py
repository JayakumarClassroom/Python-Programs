#Function - Python Bank


def get_info():
	#Get the User and Account Details
	name = input("Hello, What is your name : ").lower().strip()
	savings = float(input("How much money would you like to set up for Savings Account : "))
	current = float(input("How much money would you like to set up for Current Account : "))
	
	bank_account = {
		'name':name,
		'savings':savings,
		'current':current
		}
	return bank_account
	
def deposit(bank_account,account,money):
	#User to Deposit the money in their account
	bank_account[account] += money
	print("\nDeposited " + str(money) + " into " + bank_account['name'] + "'s " + account.lower() + " account")
	

def withdraw(bank_account,account,money):
	'''User withdrawal function'''
	#checking user have enough balance to withdraw
	if bank_account[account] - money >= 0:
		bank_account[account] -= money
		print(f"\nWithdraw Rs.{money} from {bank_account['name']}'s {account} account.")
	else:
		#Not enough balance
		print("\nSorry, Not having enough balance to Withdraw the money from the {account} account.")


def display_info(bank_account):
	'''user account function keys and value information'''
	print("\nCurrent Account Information")
	for key, value in bank_account.items():
		if key == 'name':
			print(f"{key} : {value}") 
		else:
			print(f"{key} : Rs. {value}")
	

#Main Code
my_account = get_info()

running = True
while running:
	#Show the current status of the bank information
	display_info(my_account)
	
	#Get user input for account information
	account_type = input("\nWhat account would you like to access (Savings/Current) : ").lower().strip()
	choice = input("\nWould you like to Deposit or Withdraw ?  : ").lower().strip()
	amount = float(input("\nEnter the amount for transaction : "))
	
	#make the correct function call
	if account_type == 'savings' or account_type == 'current':
		if choice == 'deposit':
			deposit(my_account, account_type, amount)
		elif choice == 'withdraw':
			withdraw(my_account, account_type, amount)
		else:
			print("Invalid option, We cannot make it Today.....")
	else:
		print("Invalid option, We cannot make it Today.....")

	try_again = input("\n\nWould you like to make another transaction ?? (y/n)  :").lower()
	if try_again != 'y':
		display_info(my_account)
		print("\n\n Thanks for using PYTHON BANK ............ ")
		running = False
	
		
