num1 = int(input("Enter the value of num1:"))
num2 = int(input("Enter the value of num2:"))
if(num1>num2):
    print("num1 is greater than num2")
    print(f"num1/num2 = {num1/num2}")
    print(f"Quotient is {(num1//num2)}")
    print(f"Remiander is {num1%num2}")
else:
    print("num1 is greater than num2")
    print(f"num1/num2 = {num2 / num1}")
    print(f"Quotient is {(num2 // num1)}")
    print(f"Remiander is {num2 % num1}")
