def new_String(String):
    if(len(user_input)<2):
        return ""
    else:
        print(f"New String is {String[:2]+String[-2:]}")

user_input = input("Enter any string:")
new_String(user_input)
