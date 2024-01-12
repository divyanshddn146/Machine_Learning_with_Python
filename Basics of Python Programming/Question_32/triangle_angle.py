# To check whether triangle is acute,obtuse, or right angled triangle
a = float(input("Enter lenght of side a:"))
b = float(input("Enter lenght of side b:"))
c = float(input("Enter lenght of side c:"))

if(a+b+c !=180):
    print("It does not form a triangle")
elif(a==90 or b==90 or c==90):
    print("It is a right angled triangle")
elif(a>90 or b>90 or c>90):
    print("It is a obtuse angled triangle")
else:
    print("It is an acute angled triangle")
