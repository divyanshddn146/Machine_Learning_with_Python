import math

num = float(input("Enter any number:"))
if(num >=0):
    print(f"Square root of {num} is {math.sqrt(num)}")
else:
    print("Square root of negative numbers does not exist")
