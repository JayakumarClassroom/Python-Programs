#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?


get_Input = int(input("Enter a value : "))
get_Division_value = int(input("Enter a Division value : "))

if get_Input % 4 ==0:
	print("its divisible by 4")
if get_Input % get_Division_value==0:
	print(f'{get_Input} is divisibly by {get_Division_value} number')
else:
	print(f'{get_Input} is not divisible by {get_Division_value} number')