#print fibonacci numbers

def fib():
	x = int(input("Enter a number to return the nth fibonacci term: "))
	f = []
	if x == 0 or x==1:
		f.append(x)
	elif x == 2:
		f = [1,1]
	elif x > 2:
		f = [1,1]
		for i in range(x-2):
			n = f[-2] + f[-1]
			f.append(n)
	return f
print (fib())