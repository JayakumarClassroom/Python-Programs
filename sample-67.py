#Function - Python Calculator App

def addition(first_number,second_number):
	add = first_number + second_number
	print(f'The Addition of Two Numbers  {first_number} + {second_number} is {add}')
	return str(first_number) + " + " + str(second_number) + " = " + str(add)

def subtraction(first_number,second_number):
	sub = first_number - second_number
	print(f'The Subtraction of Two Numbers  {first_number} - {second_number}  is {sub}')
	return str(first_number) + " - " + str(second_number) + " = " + str(sub)
	
def multiplication(first_number,second_number):
	mul = first_number * second_number
	print(f'The Multiplication of Two Numbers  {first_number} * {second_number}  is {mul}')	
	return str(first_number) + " * " + str(second_number) + " = " + str(mul)
	
def division(first_number,second_number):
	if second_number!= 0:
		div = round(first_number / second_number,4)
		print(f'The Division of Two Numbers  {first_number} / {second_number}  is {div}')
		return str(first_number) + " / " + str(second_number) + " = " + str(div)
	else:
		print('You can divide by Zero')
		return "DIV ERROR"

def exponent(first_number,second_number):
	exp = first_number ** second_number
	print(f'The Exponent of Two Numbers {first_number} ** {second_number} is {exp}')
	return str(first_number) + " ** " + str(second_number) + " = " + str(exp)

#MAIN CODE
print("Welcome to Python Calculator App")
print("Enter Two Numbers")


history = []

running = True
while running:
	num1= float(input("\nEnter a Number : "))
	num2 = float(input("Enter a Number : "))
	operator = input("\nEnter an Operation (Addition , Subtraction, Multiplication , Division or Exponent) or (A,S,M,D,E) : ").lower().strip()
	
	#call the appropriate function for calculation
	
	if operator == 'addition' or operator == 'a':
		result = addition(num1, num2)
	elif operator == 'subtraction' or operator == 's':
		result = subtraction(num1, num2)
	elif operator == 'multiplication' or operator == 'm':
		result = multiplication(num1, num2)
	elif operator == 'division' or operator == 'd':
		result = division(num1, num2)
	elif operator == 'exponent' or operator == 'e':
		result = exponent(num1, num2)
	else:
		print("Invalid variable")
		result = "OPP ERROR"
		
	history.append(result)
	
	choice = input("\nWould you like to calculate again ? (y/n) : ").lower()
	if choice != 'y':
		print("\n------ Calculation Summary ------")
		for calc in history:
			print(calc)
		print("Thanks for Playing the game !!!")
		running = False
	else:
		running = True
	

	
	