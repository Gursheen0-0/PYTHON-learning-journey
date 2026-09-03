# indexing = accessing elements of a string using index numbers. Indexing starts from 0
# and negative indexing starts from -1. 
# using [] operator
# [start:end:step]
"""no="7889881034"
print(no[0])
print(no[3:13]) 
print(no[-1])
print(no[::2])
"""
#last 4 digits of a phone number
number= input("Enter your phone number: ")
print(f"Last 4 digits of your phone number are:  {number[-4:]}")
#reverse a string
print(f"Reverse last 4 digits of your phone number is: {number[:5:-1]}")