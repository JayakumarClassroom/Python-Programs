#For loop - Quadratic Equation Solver 
import cmath


#welcome message
print("Welcome to Quadratic Equation Solver")
print("Quadratic Equation is ax^2 + bx + c = 0 ")
print("Your solution can be Real or Imaginary")
print("Your complex number is a + bj ")
print("Where a is the real portion bi is the imaginary portion")

#Get value from user
en_num=int(input("\nHow many equation would you like to solve today : "))

#loop through solve the equation
for i in range(1,en_num+1):
	print(f"\nSolving Equation # {i}")
	print("------------------------------------")
	a = float(input("Enter the coefficient of x^2 : "))
	b = float(input("Enter the coefficient of x : "))
	c = float(input("Enter the coefficient : "))
	
	#solving Quadratic Equation formula

	x1=(-b + cmath.sqrt(b**2 - 4*a*c))/(2*a)
	x2=(-b - cmath.sqrt(b**2 - 4*a*c))/(2*a)
	
	print(f"\nThe Solution to {a}x^2 + {b}x + {c} = 0")
	print(f"\n\tX1 = {x1}")
	print(f"\tX2 = {x2}")
	print("--------------------------------------------------------------------")
	
print("\nThank you for solving the Quadratic Equation. :)")