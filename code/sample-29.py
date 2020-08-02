#Chef has two positive integers A and B. He can tamper with them by choosing a digit in the decimal representation of A and a digit in the decimal representation of B and swapping these digits. This operation may be performed at most once.

#Find the maximum possible sum of the resulting numbers which Chef can obtain.

# Hello World program in Python# cook your dish here
t=int(input())
while(t!=0):
	t-=1
	a,b=[x for x in input().split()]
	ans=int(a)+int(b)                     #2 80
	if(len(a)==len(b) and len(a)==1):
		print(ans)
	elif(len(a)==1 and len(b)==2):
		ans=max(ans,int(a+b[1])+int(b[0]))
		print(ans)
	elif(len(a)==2 and len(b)==1):
		ans=max(ans,int(b+a[1])+int(a[0]))
		print(ans)
	else:
		ans=max(ans,int(b[0]+a[0])+int(b[1]+a[1]),int(a[0]+b[0])+int(a[1]+b[1]))
		print(ans)