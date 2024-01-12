n = int(input("Enter the value of n:"))

sum = 0
for i in range(1,n+1):
    sum = sum + i**2/i

print(f"Answer is {sum}")

