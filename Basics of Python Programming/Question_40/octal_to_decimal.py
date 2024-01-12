# To convert octal to decimal
decimal = input("Enter any decimal number: ")
sum = 0
d = int(decimal)

if d == 0:
    print(f"Octal value of {decimal} is 0")
else:
    i = 0
    while d != 0:
        num = d % 10
        sum = sum + num * (8 ** i)
        d = d // 10
        i += 1

    print(f"Octal value of {decimal} is {sum}")
