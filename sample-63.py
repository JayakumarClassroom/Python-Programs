#Function using local and global variable

def charac(word):
	while 'a' in word:
		word = word.replace('a','@')
	while 'e' in word:
		word = word.replace('e','3')
	while 'i' in word:
		word = word.replace('i','!')
	while 'o' in word:
		word = word.replace('o','0')
	while 'u' in word:
		word = word.replace('u','^')
	return word


phrase = 'hello, how are you today!'
print(f'Orginal String : {phrase}')
char=charac(phrase)
print(f'After Character Replacement : {char}')