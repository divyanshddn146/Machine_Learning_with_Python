# To find number of consonants and vowels in a string
user_input = input("Enter any string:")

c = 0
v = 0
for i in user_input.lower():
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        v +=1
    else:
        c += 1
print(f"Number of consonants is {c} and Number of vowels is {v}")
