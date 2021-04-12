#print prime between two intervals

prime1 = int(input("Enter the Starting Value : "))
prime2 = int(input("Enter the Ending Value : "))
	
for num in range(prime1,prime2+1):
	if num > 1:
		for i in range(2, num):
			if (num % i==0):
				break
		else:
			print(num, end='  ')
		