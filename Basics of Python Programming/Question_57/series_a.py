x = int(input("Enter value of x:"))
n = int(input("Enter the value of n:"))
sum = 0
for i in range(0,n):
    if(i%2==0):
        sum = sum + -1*(x**(i+1))
    else:
        sum = sum + x**(i+1)
print(sum)

