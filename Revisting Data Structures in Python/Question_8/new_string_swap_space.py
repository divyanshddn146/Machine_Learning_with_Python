def new_String(String1,String2):

    if(len(String1)<2 or len(String2)<2):
        return ""

    s1 = String1[:2]
    s2 = String2[:2]
    new = s2+String1[2:]+" "+s1+String2[2:]
    return new

user_input1 = input("Enter any String1:")
user_input2 = input("Enter any String2:")

s = new_String(user_input1,user_input2)
print(f"New String is {s}")
