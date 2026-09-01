#A basic return variable
def area(length, width):
    print(length*width, "in square feet")
    return length*width
def main():
    house=area(50,50)
    yard= area(20,20)
    total= house + yard
    print(total,"is total area in feet" )
main()
##############################################################
#VARIABLES: A container for a value 
#string
name="sheen"
food="pizza"
email="iamsheen@fake.com"
print(f"hello {name}")
print(f"fav food is: {food}")
print(f"email is :{email}")

#intergers
age= 22
quantity = 3
total_salary = 50000
print(f"your age is {age}")
print(f"you are buying {3} items")
print(f"your salary is : { total_salary}")

#FLOAT (decimal)
gpa = 7.4
distance = 2.2
print(f"your gpa is { gpa}")
print(f"you ran { distance} kms today")

#BOOLEAN ( True or False )
is_student = True 
print(f"are you a student: {is_student}")
if is_student:
    print("you are not a student")
else:
    print("you are not a student")

########################################################################













































    

