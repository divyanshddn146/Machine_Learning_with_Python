# To check whether all three sides of triangle are valid or not

a = float(input("Enter lenght of side a:"))
b = float(input("Enter lenght of side b:"))
c = float(input("Enter lenght of side c:"))

if(a+b<c or c+b<a or a+c<b):
    print("Lengths of triangle are not valid")
else:
    print("Lengths are valid")
