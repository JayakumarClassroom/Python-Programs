a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c =[]

for item in a:
	if item in b:
		if item not in c:
			c.append(item)
			
print("a= ", a)
print("b= ", b)
print("Items in both lists : ", c)