#Dictionary - Thesaurus App

import random

dictionary_list = {
	'hot' : ['blazing',	'boiling','heated','humid', 'scorching'],
	'cold' : ['bitter','bleak','bisk','cool','icy'],
	'happy' : ['joy','fun','cheerful','delight','glad'],
	'sad' : ['sorry','worry','heartbroken','dismal','somber']	
}

print("Welcome to Thesaurus App")
print("\nChoose a word from the Thesaurus App and I will give you a synonym.")

#printing the Thesaurus list
print("\nHere are words in the Thesaurus App")
for i in dictionary_list.keys():
	print(f"\t{i}")

choice = input("\nWhat word would you like a Synonym for : ").lower()

rand_choice = random.randint(0,4)
if choice in dictionary_list.keys():
	'''
	for new in dictionary_list.values():
		print(f'A Synonym for {choice} is {new[rand_choice]}')
		break
	'''
	print(f'A Synonym for {choice} is {dictionary_list[choice][rand_choice]}')

see_dict_list = input("Would you like to see the Whole thesaurus app list (Y/N): ").lower()

if see_dict_list == 'y':
	for k,v in dictionary_list.items():
		print(f'{k.title()} Synonyms are :')
		for n in v: 
			print(f'\t{n}')
else:
	print("Thank you for using Thesaurus App")