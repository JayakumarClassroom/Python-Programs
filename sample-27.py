#Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

#Extra:
#Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.


def simplePassword():
	random.seed(random.choice(words))
	x=list(random.choice(words))
	x[random.randint(0,7)]=str(random.randint(0,99))
	return "".join(x)
	

def averagePassword(n):
	random.seed(random.choice(words))
	random.shuffle(avg)
	pwd=[random.choice(avg) for x in range(n)]
	return "".join(pwd)
	


def strongPassword(n):
	random.seed(random.choice(words))
	random.shuffle(strz)
	pwd=[random.choice(strz) for x in range(n)]
	return "".join(pwd)
	




import random

words=['actually', 'expected', 'property', 'addition', 'followed', 'provided', 'although', 'happened', 'question', 'american', 'increase', 'received', 'anything', 'industry', 'religion', 'building', 'interest', 'remember', 'business', 'involved', 'required', 'children', 'national', 'services', 'complete', 'organize', 'southern', 'consider', 'personal', 'standard', 'continue', 'planning', 'strength', 'couldnt', 'position', 'students', 'decision', 'possible', 'suddenly', 'directly', 'pressure', 'thinking', 'district', 'probably', 'together', 'economic','problems', 'training', 'evidence', 'programs']
strz=list("!)*+,-./0126789:;<=>DEF?@ABCGHI#$%&\(JKLMNOPQRSTUVWXYZab@ABCGHI#$%&\(JKLMNOcdefg345hijklmnopqrstuvwxyz")
avg=list("ahijklbcd0123456789efgmnopqrstuvwxyz0123456789")

while True:
	print ("how strong your password should be?")
	print ("'simple' , 'average', or 'strong'?")

	x=input("\n")
	print ("")
	if x=="simple":
		print ("your password is: ", simplePassword())
		break
	elif x=="average":
		i=int(input("how many characters your password should have?: "))
		print("your password is: ", averagePassword(i))
		break
	elif x=="strong":
		i=int(input("how many characters your password should have?: "))
		print("your password is: ", strongPassword(i))
		break
	else:
		pass