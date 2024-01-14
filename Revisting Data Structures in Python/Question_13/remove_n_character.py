def remove_character(s,i):
    if(len(s)<1):
        return ""
    elif(i>len(s)-1 or i<-len(s)):
        return "Wrong index entered"
    else:
        new = s[:i] + s[i+1:]
        return new

user_input = input("Enter any string:")
index = int(input("Enter any index:"))
result = remove_character(user_input,index)
print(f"{result}")
