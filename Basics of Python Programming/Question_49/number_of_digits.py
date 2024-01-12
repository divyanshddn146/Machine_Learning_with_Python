num = int(input("Enter any number:"))
count = 0
n = num
while(num!=0):
    num=num//10
    count = count +1
print(f"Number of digits in {n} is {count}")

