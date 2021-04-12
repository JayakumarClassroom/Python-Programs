#Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

import random
password = 'qwertyuiop[]asdfghjkl;zxcvbnm!@#$%^&*()_+=-QWERTYUIOPLKJHGFDSAZXCVBNM,./?><1234567890~`'
val=''
while val!='exit':
	val=input("Press enter to get new password or enter exit ")
	if val=='':
		randomvalue = random.sample(password,15)
		randomvalue_1 = ''.join(randomvalue)
		print(randomvalue_1)
	elif val=='exit' or 'EXIT':
		break
		exit()
	