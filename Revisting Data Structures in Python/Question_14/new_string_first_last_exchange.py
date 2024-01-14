def new_string(s):
    if(len(s)<2):
        return s
    new = s[len(s)-1] + s[1:-1] + s[0]
    return new

user_input = input("Enter any string:")
result = new_string(user_input)
print(f"{result}")
