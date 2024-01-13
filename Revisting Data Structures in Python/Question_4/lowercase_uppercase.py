# To find number of lowercase and uppercase letters in a string
user_input = input("Enter any string:")

l = 0
u = 0
for i in user_input:
    if(i.islower()):
        l +=1
    elif(i.isupper()):
        u += 1
    else:
        continue
print(f"Number of lowercase letters are {l} and Number of uppercase letters are {v}")
