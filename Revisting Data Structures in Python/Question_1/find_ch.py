def find_ch(x,String,c):
    for i in range(x,len(String)):
        if(c == String[i]):
            return i
    return -1

user_input = input("Enter any string:")
char_to_find = input("Enter any character:")
position = int(input("Enter any specific position:"))


result = find_ch(position,user_input,char_to_find)

if(result>0):
    print(f"Resulting index is {result}")
else:
    print("Character not found")
