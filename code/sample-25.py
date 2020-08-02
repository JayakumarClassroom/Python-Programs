#Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.

def strfunc(n):
	a=n.split()
	b=a[::-1]
	return (' '.join(b))

n=input("Enter the string : ")
print(strfunc(n))

