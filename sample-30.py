#Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference

def func(get_input):

	if get_input < 17:
		return 17-get_input
	else:
		val = get_input-17
		val = val*2
		return val
	
print(func(int(input("Enter a val : "))))