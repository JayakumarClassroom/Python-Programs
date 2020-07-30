#Dictionary - Frequency Analysis App 
from collections import Counter

print("welcome to Frequency Analysis App ")

#non letters need to remove from the phrase
non_letters = ['1','2','3','4','5','6','7','8','9','!','0','.','?',')','(','*','&','%','$','#','@','\n','\t',' ',',',';',':','"',"'"]

key_phrase_1 = input("Enter a phrase to count the occurence of each letter: ").lower().strip()

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

for letter in key_phrase_1_order_count:
	print(letter, end=' ')




