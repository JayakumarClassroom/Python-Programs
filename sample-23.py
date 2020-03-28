#Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

def listfunc(n):
	a=set(n)
	print(list(a))

listfunc([1,2,3,4,5,1,3,5,7,9,1,2])