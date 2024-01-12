n = int(input("Enter value of n:"))
a = 0
b = 1
if(n==1):
    print(0)
elif(n==2):
    print(1)
elif(n>2):
    for i in range(n-2):
        temp = b
        b = a + b
        a = temp
    print(b)

