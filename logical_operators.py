#logical operators are the operators that are used to combine conditional statements.
# or = atleast one condition must be true
# and = both conditions must be true
# not= Inverts the boolean value of the condition
"""
#OR OPERATOR
print("this is for the OR operator")
temp= float(input("enter the temperature:"))
is_raining= False
if temp>30 or temp<0 or is_raining:
    print("the event is cancled")
else:
    print("you can still go play outside:")
"""


#and-not OPERATOR
print("this is for the AND-NOT operator")

temp = int(input("enter the temperature:"))
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT outside 🥵")
    print("It is SUNNY ☀️")

elif temp <= 0 and is_sunny:
    print("It is COLD outside 🥶")
    print("It is SUNNY ☀️")

elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside 🙂")
    print("It is SUNNY ☀️")

elif temp >= 28 and not is_sunny:
    print("It is HOT outside 🥵")
    print("It is CLOUDY ☁️")

elif temp <= 0 and not is_sunny:
    print("It is COLD outside 🥶")
    print("It is CLOUDY ☁️")

elif 28 > temp > 0 and not is_sunny:
    print("It is WARM outside 🙂")
    print("It is CLOUDY ☁️")

