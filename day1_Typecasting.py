#Typecasting: converting one varibale into another
name = "sheen"
print(type(name))
age = 22
print(type(age))
gpa=7.4
print(type(gpa))
is_student= True
print(type(is_student))
print(age+3)
 
#change the datatype.....
gpa=int(gpa)
print(gpa)
print("your gpa's datatype is:",type(gpa))

age= float(age)
print(age)
print("your age's data type is:",type(age))

age=str(age)
print(age)
print("age's datatype is:" ,type(age))
#now print(age+3) will show error as age is now a string
age+="1"
print(age)

name=bool(name)
print(name)
