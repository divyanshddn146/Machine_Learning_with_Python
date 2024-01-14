def new_string(s):
    if(len(s)<1):
        return ""
    new = ""
    for i in range(0,len(s)):
        if(i%2==0):
            new = new + s[i]
    return  new

user_input = input("Enter any string:")
result = new_string(user_input)
print(f"{result}")
