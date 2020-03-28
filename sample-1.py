#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

get_Name = input("Enter your Name : ")
get_age = int(input("Enter your Age : "))

sum_of_age = 100 - get_age
age_at_100 = 2020 + sum_of_age

print(f'Hello {get_Name}, current age is {get_age}. \nYour 100th Birthday year is {age_at_100}')