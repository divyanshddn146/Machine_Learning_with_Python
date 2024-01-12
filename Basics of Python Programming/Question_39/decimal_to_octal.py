# To convert decimal to octal
decimal = input("Enter any decimal number: ")
sum = 0
d = int(decimal)

if d == 0:
    print(f"Octal value of {decimal} is 0")
else:
    i = 0
    while d != 0:
        num = d % 8
        sum = sum + num * (10 ** i)
        d = d // 8
        i += 1

    print(f"Octal value of {decimal} is {sum}")
