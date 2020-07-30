a=['a','b','c','d','e']
b=[1,2,3,4,5]
c=[1.0,2.2,3.3,4.5,4.5]

for i,j,k in zip(a,b,c):
	print(i + " : " + str(j) + " : " + str(k))