def new_String(string):

    if(len(string)<3):
        return string
    elif(string.endswith("ing")):
        new = string.replace("ing","ly")
        return new
    else:
        new = string + "ing"
        return new

user_input = input("Enter any String:")
s = new_String(user_input)

print(f"New string is {s}")
