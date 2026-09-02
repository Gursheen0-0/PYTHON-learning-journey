#if : only if something is true  
#else: some other thing is true
age=int(input("Enter your age: "))

if age>19:
    print("WOW! YOU ARE AN ADULT")
elif age<13:
    print("you are a BABY")
else:
    print("you are a Teenager")
