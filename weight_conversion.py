weight = float(input("Enter your weight : "))
unit= (input("Enter your unit (kg/lb) : "))
if unit == "kg":
    weight = weight * 2.205
    unit = "lb"
    print(f"Your weight is {weight} {unit}")
elif unit == "lb":
    weight = weight/2.205
    unit = "kg"
    print(f"Your weight is {weight} {unit}")
else:
    unit != "kg" or unit != "lb"
    print("Invalid unit")

