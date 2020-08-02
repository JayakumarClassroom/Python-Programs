#for loop - fibonacci sequence program

print("Welcome to fibonacci sequence program ")

num=int(input("Enter the number to compute the fibonacci sequence : "))

#compute the fibonacci sequence
fib=[1,1]
for i in range(num-2):
	n=fib[i]+fib[i+1]
	fib.append(n)
print(fib)