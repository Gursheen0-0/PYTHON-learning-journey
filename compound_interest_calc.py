#compound interest calculator
#A= final amount
#P= initial amount
#r= rate of interest
#t= numbers of time period
principle=0
interest=0
time=0
while principle<=0:
    principle=float(input("Enter the principle amount: "))
    if principle<=0:
        print("Principle cannot be Negative or Zero")

while interest<=0:
    interest=float(input("Enter the interest rate: "))
    if interest<=0:
        print("interest rate cannot be Negative or Zero")

while time<=0:
    time=int(input("Enter the time in years : "))
    if time<=0:
        print("time cannot be Negative or Zero")

print("principle Amount is :",principle)
print("rate or interest is :" ,interest)
print(f"time is {time} years")

total= principle * (pow(1+interest/100,time))
print(f"YOUR TOTAL AMOUNT AFTER {time} YEARS WITH {interest} INTEREST IS: {round(total,3)}")