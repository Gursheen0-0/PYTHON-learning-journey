operator=input("Enter the operator (+, -, *, /): ")
a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
if operator == "+":
    result = a + b
    print (f"the result ot {a} + {b} is: {round(result, 2)}")
elif operator == "-":
    result = a - b
    print (f"the result ot {a} - {b} is: {round(result, 2)}")
elif operator == "*":
    result = a * b
    print (f"the result ot {a} * {b} is: {round(result, 2)}")
elif operator == "/":
    result = a / b
    print (f"the result ot {a} / {b} is: {round(result, 2)}")
else:
    print("Invalid operator. Please use +, -, *, or /")