a=int(input("ENTER THE 1st NUMBER: "))
b=int(input("ENTER THE 2nd NUMBER: "))
c=int(input("ENTER THE 3rd NUMBER: "))
d=int(input("ENTER THE 4th NUMBER: "))
if(a>b and a>c and a>d):
    print("a is the biggest number")
elif(b>a and b>c and b>d):
    print("b is the biggest number:")
elif(c>a and c>b and c>d):
    print(" c is the biggest number:")
else:
    print("d is the biggest number:")
