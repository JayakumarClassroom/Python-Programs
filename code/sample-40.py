#For loop - Binary/Hexadecimal Converstion


print("Welcome to Binary/Hexadecimal Converstion")

#Get the user input and generate list
max_value = int(input("Enter the decimal value to compute : "))
decimal = list(range(1,max_value+1))

binary=[]
hexadecimal=[]

#bin() hex() for converstion 

for num in decimal:
	binary.append(bin(num))
	hexadecimal.append(hex(num))
print("Generating list....... Completed !!!")

#slicing index from user 
print("\nUsing slice, we will show a portion of each list")
low_range=int(input("Enter the starting position number : "))
up_range=int(input("Enter the ending position number : "))

#slice through list individually
print(f"\nDecimal Values from {low_range} to {up_range} :")
for i in decimal[low_range:up_range]:
	print(i)

print(f"\nBinary Values from {low_range} to {up_range} :")
for i in binary[low_range:up_range]:
	print(i)
	
print(f"\nHexadecimal Values from {low_range} to {up_range} :")
for i in hexadecimal[low_range:up_range]:
	print(i)

#Output the whole list to the screen
input(f"\nPress ENTER key to display all the value from 0 to {max_value}.")
print("Decimal ......... Binary ............. Hexadecimal")
print("............................................................")

for x,y,z in zip(decimal,binary,hexadecimal):
	print(f"\t{x}...\t...{y}...\t...{z}")