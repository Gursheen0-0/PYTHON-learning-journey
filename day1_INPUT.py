while True:
    name = input("what is your name ?" )
    age = int(input ("How old are you?:"))
    print(f"HELLO {name}! WELCOME to my python code")
    if age>25:
        print("you old af haha")
    else:
        print("aww u such a bby")
        choice=input("\n if u wanna continue (y/n)??: ")
        if choice.lower() == "n":
            print("bie bie pookie ;)")
            break
