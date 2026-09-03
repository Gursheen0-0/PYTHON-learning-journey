"""
 
#1
name= input("Enter your name: ")
while name == "":
    print("you did not type your name, please try again")
    name = input("Enter your name: ")
print(f"Hello {name}, welcome!")
"""
"""
#2
age=int(input("Enter your age: "))
while age<0:
    print("Age cannot be negative, pls try again:")
    age = int(input("Enter your age: "))
print(f"You are {age} years old.")
"""
"""
#3
number=int(input("Enter a number between 0 and 100:"))

while number<0 or number>100:
    print("Number is out of range, please try again:")
    number=int(input("Enter a number between 0 and 100:"))
print(f"Your Number is {number}")
"""