#Take Randomly generate two lists and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

import random

first_list= random.sample(range(100,200,3),10)
second_list=random.sample(range(200),13)

print (first_list)
print (second_list)

common_numbers= []

for num in first_list:
	if num in second_list:
		common_numbers.append(num)

print (common_numbers)