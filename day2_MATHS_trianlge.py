import math
A =float(input("Enter the value of a: "))
B =float(input("Enter the value of b: "))
# for the hypotenuse of a  rigth angled triangle

HYPOTENUSE = math.sqrt(A**2 + B**2)
print("The hypotenuse of the triangle is:", round(HYPOTENUSE,3))
#or
#HYPOTENUSE1 = math.hypot(A, B)
#print("The hypotenuse of the triangle is:", round(HYPOTENUSE1,3))

