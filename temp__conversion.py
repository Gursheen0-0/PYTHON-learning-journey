unit=(input("Enter the temerature unit (c/f) : "))
measurement = float(input("Enter the temperature : "))
if unit == "c":
    measurement = (measurement * 9/5) + 32
    unit = "F"
    print(f"The temperature is {measurement} {unit}")
elif unit == "f":
    measurement = (measurement - 32) * 5/9
    unit = "C"
    print(f"The temperature is {measurement} {unit}")
else:
    print("Invalid unit")