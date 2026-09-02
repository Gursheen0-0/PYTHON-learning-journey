#validate user input 
#username is no more than 12 characters
#no spaces in the username
#no special characters and digits
username=input("Enter your username: ")
if len(username) > 12:
    print("Username must be no more than 12 characters.")
elif " " in username:
    print("Username must not contain spaces.")
elif not username.isalpha():
    print("Username must not contain special characters or digits.")
else:
    print(f"Username '{username}' is valid.")