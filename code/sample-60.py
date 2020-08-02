# While Loop - Guess My Word App

import random

print("Welcome to Guess My Word App")

#word list for the games
word_list = {
	'sports':['tennis','cricket','football','volleyball','hockey'],
	'fruits':['watermelon','strawberry','mango','apple','pineapple','lemon'],
	'colors':['yellow','black','white','purple','grey','sandal','pink'],
	'clothing':['jeans','tshirt','shirt','trouser','belt','watch']
}


#creating Dictionary KEY list
word_key=[]
for key in word_list.keys():
	word_key.append(key)

#intializing the main while loop
playing = True
while playing:
	#Generating Random key and value
	ran_word_key = word_key[random.randint(0,len(word_key)-1)]
	ran_word_value = word_list[ran_word_key][random.randint(0,len(word_list[ran_word_key])-1)]
	#print(ran_word_value)
	
	#replacing the word with dashes (-) 
	blank_word=[]
	for val in ran_word_value:
		blank_word.append('-')
		
	print(f'Guess a {len(ran_word_value)} letter word from the following catergory: {ran_word_key.title()} ')
	
	guess=''
	guess_count=0
	
	#A single round loop
	while guess != ran_word_value:
		print(''.join(blank_word))
		guess = input("\nEnter your Guess : ").lower().strip()
		guess_count += 1
		
		if guess == ran_word_value:
			print(f'You Guessed Correctly in {guess_count} guesses.')
		else:
			print('That is not correct. let us reveal a letter to help you')
			
			#swapping while loop
			
			swapping = True
			while swapping:
				letter_index = random.randint(0,len(ran_word_value)-1)
				if blank_word[letter_index] == '-':
					blank_word[letter_index] = ran_word_value[letter_index]
					swapping = False
				
			
	#Do you want to play agian
	choice = input("Do you want to play again (Y/N).... ? ").lower()
	if choice != 'y':
		print("Thanks for playing")
	