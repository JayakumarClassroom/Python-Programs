#19. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged. Go to the editor

get_input=input("Enter the string : ").lower()
val=get_input.startswith('is')
if val == True:
	print(get_input)
else:
	print('is'+get_input)
