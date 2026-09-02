name=input("Enter your full name: ")

length=len(name)
print(f"Your name has {length} characters")

#name = name.count("e")
#print(name)

digits = name.isdigit()
print(digits)

name = name.upper()
print(name)

name = name.lower()
print(name)

name=name.capitalize()
print(name)

search= name.find("e")
print(f"The first occurrence of 'e' is at index {search}")

search= name.rfind("e")
print(f"The last occurrence of 'e' is at index {search}")

name = name.replace("e", "a")
print(name)

name = name.strip()
print(name)
 
#and many more string methods are available in python. 
#print(help(str))
"""
s = "Hello, my name is Sheen and I love Python programming!  "
print(s.capitalize())
print(s.endswith("  "))
print(s.startswith("He"))
print(s.casefold())
print(s.find("S"))
print(s.swapcase())
print(s.strip())
print(s.isupper())
print(s.title())
print(s.index("Sheen"))
"""