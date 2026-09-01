while True:
    a=int(input("type the first number: "))
    b=int(input("type the second number: "))
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    print("your final answer is: ")
    print("sum:" ,sum,"\nsub" ,sub,"\nmul", mul ,"\ndiv", div)
    choice = input("\nDO u want to coninue again (Y/n)?")
    if choice.lower()=="n":
         print("okie ji :)")
         break
