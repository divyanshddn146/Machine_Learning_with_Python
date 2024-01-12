# To display all numbers that are not divisible by 7 and 11
for i in range(1,101):
    if(i%7==0 and i%11==0):
        continue
    else:
        print(i)

