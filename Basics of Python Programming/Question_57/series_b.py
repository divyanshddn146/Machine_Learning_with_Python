x = int(input("Enter value of x:"))
n = int(input("Enter the value of n:"))
sum = 0
def factorial(z):
    result = 1
    if(z==0):
        return 1
    if(z>0):
        for i in range(1,z+1):
            result = result * i
        return result
for i in range(0,n):
    if(i%2 == 0):
        sum = sum + (x**i)/factorial(i)
    else:
        sum = sum + (-1*(x**(i)))/factorial(i)
print(sum)

