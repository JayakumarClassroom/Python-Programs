#Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

#Extras:
#Write two different functions to do this - one using a loop and constructing a list, and another using sets.
#Go back and do Exercise 5 using sets, and write the solution for that in a different function.

l=[]
def listfunc(n):
	for x in range(n):
		l.append(int(input("Enter a value : ")))
	return l

def setfunc(n):
	return list(set(l))

n=int(input("Enter the value : "))
print(listfunc(n))
print(setfunc(n))


