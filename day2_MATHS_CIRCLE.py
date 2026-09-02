#for a circle, the circumference is calculated using the formula C = 2 * π * r
#ARea of a circle is calculated using the formula A = π * r^2
import math
radius1 = float(input("Enter the radius of the circle for circumference: "))
radius2 = float(input("Enter the radius of the circle for area: "))
circumference = 2 * math.pi * radius1

area = math.pi * radius2 ** 2

print("The circumference of the circle is:", round(circumference,3))
print("The area of the circle is:",round(area,3) )
