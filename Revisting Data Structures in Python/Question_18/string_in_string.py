def string_in_string(s1,s2):
    if(len(s1)%2==0):
        x = int(len(s1)/2)
        return s1[0:x] + s2 + s1[x:]
    else:
        x = int(len(s1)+1/2)
        return s1[0:x-1] + s2 + s1[x-1:]



s1 = input("Enter string:")
s2 = input("Enter string to be inserted:")
result = string_in_string(s1,s2)
print(result)
