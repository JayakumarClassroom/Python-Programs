#For loop - Factoral Program
import math 

print("Welcome to the Factorial Program App")

#getting the user input value 
fact_num=int(input("Enter the number to calculate the Factorial Program : "))

print(f'{fact_num}!',end=' ')
for i in range(1, fact_num):
	print(f'{i}', end='*')
print(fact_num)

#using math library 
fact=math.factorial(fact_num)
print("\nHere is the result from the Math Library")
print(f'The Factorial of {fact_num} is {fact}')

print("\n-----------------------------------------------")

#using the manual method for calculating the factorial
fact_man=1
for i in range(1,fact_num+1):
	fact_man = fact_man*i
print("\nManual method for calculating the factorial")
print(f'The Factorial of {fact_num} is {fact_man}')
	