#Prime number using while program
import time 

print("Welcome to Prime number program")

running = True
while running:
	print("\nEnter 1 to determine if a specific number is prime or not")
	print("Enter 2 to determine all the prime numbers within a set of range")
	choice = int(input("Enter your choice 1 or 2 : "))
	
	#checking prime for individual numbers
	if choice == 1:
			choice_1 = int(input("\nEnter a number to determine it is prime or not : "))
			
			prime_status = True
			for i in range(2,choice_1):
				print(i)
				if choice_1 % i ==0:
					prime_status = False
					break
			if prime_status:
				print(f'{choice_1} is prime')
			else:
				print(f'{choice_1} is NOT prime')
	
	#Deterime the prime between two numbers
	elif choice == 2:
		lower_bound=int(input("\nEnter the lower bound number : "))
		upper_bound=int(input("Enter the upper bound number : "))
		primes = []
		
		#time calculation 
		start_time=time.time()
		
		#prime status of lower and upper bound
		
		
		for prime_check in range(lower_bound,upper_bound+1):
			if prime_check > 1:
				prime_status = True
				for i in range(2, prime_check):
					if prime_check % i ==0:
						prime_status = False
						break
			else:
				prime_status = False
				
			if prime_status:
				primes.append(prime_check)
		
		#get the current time 
		stop_time = time.time()
		
		#time calculation
		calculation_time = stop_time-start_time
		calculation_time = round(calculation_time,4)
		
		print(f"\nCalculation took a total of {calculation_time} seconds.")
		print(f"\nThe following numbers between {lower_bound} and {upper_bound} are prime : ")
		
		new_choice = input("Press ENTER KEY to continue")
		for prime in primes:
			print(prime)
	
	else:
		print("\nThat is not a VALID OPTION")		
	
	quit = input("Do you want to Try Again ?? (Y/N)   : ")
	if quit != 'y':
		running=False
		print("Thank you for trying this program")

