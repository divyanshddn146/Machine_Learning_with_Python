def new_String(String):

    if(len(String)<1):
        return ""

    f = String[0]
    new = String[0]

    for i in String[1:]:
        if (i != f):
            new = new + i
        else:
            new = new + '$'

    return new

user_input = input("Enter any String:")

s = new_String(user_input)
print(f"New String is {s}")
