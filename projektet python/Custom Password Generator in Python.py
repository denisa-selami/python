import random
letters = ['a', 'b', 'c', 'd']
numbers = ['1', '2', '3', '4', '5']
symbols = ['?', '$', '%', 'x']
 
print("Welcome to the pygeneration password!")
nr_letters = int(input("how many letters would you like to put in your password?\n"))
nr_symbols = int(input(f"how many symbols you like?\n"))
nr_numbers = int(input(f"how many numbers would you like?\n"))

password = ""

for char in range (nr_letters ):
    password += random.choice(letters)
for char in range (nr_symbols) :
    password += random.choice(symbols)
for char in range (nr_numbers) :
    password += random.choice(numbers)

print(f"your generated pasword is: {password}")