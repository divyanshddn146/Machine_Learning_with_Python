# To find number of lowercase and uppercase letters in a string
user_input = input("Enter any string:")

d = 0
a = 0
s = 0

for i in user_input.lower():
    if(i.isalpha()):
        a +=1
    elif(i.isdigit()):
        d += 1
    elif(i.isspace()):
        s += 1
    else:
        continue

print(f"Number of alphabets are {a} and Number of digits are {d} and Number of spaces are {s}")
