#for loop - Grade Point Average Calculator App

print("welcome to Grade Point Average Calculator App")

#Get name and Number of Grades
name=input("\nWhat is your name : ").title()
num=int(input("How many grades would you like to enter : "))

#Enter the grades using for loop
grade_list=[]
for i in range(1,num+1):
	grade_list.append(int(input("Enter grade : ")))

#Display grades in Highest to lowest 

#grade_list.sort(reverse=True) #this method also fine 

print("Grades Highest to Lowest :")
for i in sorted(grade_list, reverse=True):
	print("\t",i)
	
#Summary of the student
print(f"\n{name}'s Grade Summary : ")
print(f"\tTotal Number of Grades: {num}")
print("\tHighest Grade: ", max(grade_list))
print("\tLowest Grade: ", min(grade_list))

#calculate the average
avg_sum=sum(grade_list)
avg=avg_sum/num
avg=round(avg,2)
print("\tAverage Grade: ",avg)

#Desired average
des=float(input("\nWhat is your desired  average : "))

grade_req=des*(len(grade_list)+1)-sum(grade_list)
grade_req=round(grade_req,2)

print(f'\nGood Luck {name}!')
print(f'You will need to get a {grade_req} on your next assignment to earn a {des} average.')

#copying the grades list from old to new list
new_grade_list=grade_list[:]
#changing the grades 
print("\nLet see what your average could have been if you did better/worse on an assignment.")
old_grade=int(input("What grades do you like to change : "))
new_grade=int(input(f"What grades do you like to change from {old_grade} to: "))

new_grade_list.remove(old_grade)
new_grade_list.append(new_grade)

#printing new grades 
print("\nNew Grades Highest to Lowest:")
for i in sorted(new_grade_list, reverse=True):
	print("\t",i)

#Summary of the student
print(f"\n{name}'s New Grade Summary : ")
print(f"\tTotal Number of Grades: {num}")
print("\tHighest Grade: ", int(max(new_grade_list)))
print("\tLowest Grade: ", int(min(new_grade_list)))

#calculate the average
new_avg_sum=sum(new_grade_list)
new_avg=new_avg_sum/num
new_avg=round(new_avg,2)
print("\tAverage Grade: ",new_avg)


#Comparing old and new Grades change

print(f"\nYOur new average would be a {new_avg} compared to your real average of {avg}!")
avg_change = new_avg-avg
avg_change = round(avg_change,2)
print(f"That is a change of {avg_change} points!")

#Too bad the orginal grades are still intact!!!
print("\nToo bad the orginal grades are still the same!!")
grade_list.sort(reverse=True) #this method also fine 
print(grade_list)
print("You should go ask for extra credit!")