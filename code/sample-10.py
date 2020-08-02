#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.) eg: mom, 


get_Input =input("Enter a string to check the palindrom : ") #my mother

val1 = get_Input.replace(" ","")
check_pali =  val1[::-1]

if check_pali == val1:
	print("Its a palindrome")
else:
	print("Not a palindrom")
