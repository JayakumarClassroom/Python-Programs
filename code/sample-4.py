#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)


get_Input = int(input("Enter a Number : "))
list_word = []
for i in range(1,50):
	if i % get_Input == 0:
		list_word.append(i)

print(list_word)