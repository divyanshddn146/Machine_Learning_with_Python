m = int(input("Enter value of m:"))
n = int(input("Enter value of n:"))
if(m<=n):
    for i in range(1,n):
        if(i%m==0):
            print(i,end=' ')
else:
    print("Invalid Value")
