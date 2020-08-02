#Dictionary - Code Breaker App 

from collections import Counter

print("welcome to Code Breaker App ")

#non letters need to remove from the phrase
non_letters = ['1','2','3','4','5','6','7','8','9','!','0','.','?',')','(','*','&','%','$','#','@','\\n','\\t',' ',',',';',':','"',"'",'-','/','\\',',']


#hard code a pre determined key phrase
key_phrase_1 = "Machine learning is a part of the data science which do predictive analysis on the given data and provide us outcomes by making automatic learning by searching patterns in the data which is accessing by its algorithms and programmed accordingly. Random Forest Algorithm is the most sought-after machine learning algorithm. It is used for both Classification and Regression problems. Like other machine learning algorithms, it is used to predict the assertive outcomes based on the labelled data given. Many decision trees combine to form a forest which is the prime focus of Random Forest algorithm. The number of trees the more powerful the forest is or in other words we can say the number of trees the more accurate the results after aggregating will be.The Naive Bayes algorithm is a probabilistic classifier that determine an arrangement of probabilities by checking the rotation and mix of qualities in a given dataset. Naive Bayes demonstrate is anything but difficult to build and especially helpful for candid information collections. Alongside inactivity, Naive Bayes is known to highly sophisticated classification methods. Bayes theorem gives a method for calculating posterior probability. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborumzzzzz.".lower()

#Removing all non letters from the key phrase 
for nonlett in non_letters:
	key_phrase_1=key_phrase_1.replace(nonlett,'')

total_occurs = len(key_phrase_1)

#create a counter object to tally the number of each letter 
letter_count = Counter(key_phrase_1)

#calculate the percentage of each letters

print("\nHere is the frequency analysis from key phrase -1 :")
print("\n\tLetter \t\tOccurrence \tPercentage")
for key,value in sorted(letter_count.items()):
	percentage = 100*value/total_occurs
	percentage = round(percentage,2)
	print(f"\t{key}\t\t{value}\t\t{percentage}%")

ordered_letter_count = letter_count.most_common()
key_phrase_1_order_count = []
for pair in ordered_letter_count:
	key_phrase_1_order_count.append(pair[0])

print("\nLetters ordered from highest occournce to lowest: ")

for letter_1 in key_phrase_1_order_count:
	print(letter_1, end='')

#--------------------------------------------------------------------------------------------------

print("\n\n\n")

key_phrase_2 = "This is the first module of our project. The important role for the cloud user is to move login window to cloud user window. This module has created for the security purpose. In this login page we have to enter login user id and password. It will check username and password is match or not (valid user id and valid password). If we enter any invalid username or password we cant enter into login window to user window it will shows error message.  So we are preventing from unauthorized user entering into the login window to user window. It will provide a good security for our project. So server contain user id and password server also check the authentication of the user. It well improves the security and preventing from unauthorized user enters into the network. In our project we are using JSP for creating design. Here we validate the login user and server authentication. This is the module for sentimental analysis that is began with a lexicon of words with established prior polarities, and identifies the contextual polarity of phrases, based on some refined annotations. We combined different kinds of negators with lexical polarity items though various compositional semantic models, both heuristic and machine learned, to improved sub sentential sentiment analysis Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.".lower()

#Removing all non letters from the key phrase 
for nonlett in non_letters:
	key_phrase_2=key_phrase_2.replace(nonlett,'')

total_occurs = len(key_phrase_2)

#create a counter object to tally the number of each letter 
letter_count = Counter(key_phrase_2)

#calculate the percentage of each letters

print("\nHere is the frequency analysis from key phrase - 2 :")
print("\n\tLetter \t\tOccurrence \tPercentage")
for key,value in sorted(letter_count.items()):
	percentage = 100*value/total_occurs
	percentage = round(percentage,2)
	print(f"\t{key}\t\t{value}\t\t{percentage}%")

ordered_letter_count = letter_count.most_common()
key_phrase_2_order_count = []
for pair in ordered_letter_count:
	key_phrase_2_order_count.append(pair[0])

print("\nLetters ordered from highest occournce to lowest: ")

for letter_2 in key_phrase_2_order_count:
	print(letter_2, end='')

#Encode or decode a given mesage using the key phrase 1 and key phrase 2

choice = input("\n\nWould you like to Encode or Decode a message :").lower()
phrase = input("What is the Phrase for Encode or Decode : ").lower()

for nonlett in non_letters:
	phrase=phrase.replace(nonlett,'')

#encode a mesage
if choice == 'encode':
	encoded_phrase = []
	for letter in phrase:
		index = key_phrase_1_order_count.index(letter)
		letter = key_phrase_2_order_count[index]
		encoded_phrase.append(letter)
	print("\nThe Encoded message is : ")
	for letter in encoded_phrase:
		print(letter,end='')

#decode a message
elif choice == 'decode':
	decoded_phrase=[]
	for letter in phrase:
		index = key_phrase_2_order_count.index(letter)
		letter = key_phrase_1_order_count[index]
		decoded_phrase.append(letter)
	print("\nThe Decoded message is : ")
	for letter in decoded_phrase:
		print(letter,end='')

else:
	print("Encode or Decode the message, Try again")
