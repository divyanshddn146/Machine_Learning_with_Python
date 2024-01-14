def new_String(s):
    i1 = s.find("not")
    i2 = s.find("poor")

    if(i1 != -1 and i2 != -1 and i1<i2):
        i3 = s.find("bad",i2)
        if(i3 != -1):
            s = s[:i1] + "good" + s[i3+3:]
            return s

user_input = input("Enter any String:")
s = new_String(user_input)

print(f"{s}")
