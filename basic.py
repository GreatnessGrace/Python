# 1️⃣  Python Version

# python --version

# 2️⃣ print in python

print("Hello, World!")
# 💡 The print() function is used to display output.


# 3️⃣ variables and data types

x = 10 # integer

y = 10.5 # float

name = "Ankush" # string

is_student = True  # boolean

fruits = ["apple", "banana", "cherry"] # list mutable

fruits2 = ("apple", "banana", "cherry") # tuple immutable

person = {"name": "Ankush", "age": 25} # dictionary , key: value pairs

# 4️⃣ Input

name = input("Enter ur name: ")

print("Hello, " + name + "!")

# 📝 input() takes user input as a string.


# 5️⃣  Conditional Statements

age = int(input("Enter ur age: "))

if age >= 18:
    print("You are an adult!")
elif age > 12:
    print("You are a teenager!")
else: 
    print("you are a kid!")

# 💡 Python uses indentation (spaces/tabs) instead of {} for code blocks.

# 6️⃣ Loops

# 🔹 For Loop

for i in range(5):
    print("The value of the number is:", i)

#  🔹 While Loop

x = 0

while x < 5:
    print("The value of x is:", x)
    x += 1 

# 7️⃣ Functions

def greet(name):
    return "Hello, " + name + "!"

print(greet("Ankush"))

# 💡 Functions in Python are defined using def.



