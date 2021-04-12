#Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2. 

get_string = input("Enter a string : ")
get_input= int(input("Enter a value : "))
len_str = len(get_string)
c = get_string[:2]
if len_str==2:
	print(get_string*get_input)
else:
	print(c*get_input)