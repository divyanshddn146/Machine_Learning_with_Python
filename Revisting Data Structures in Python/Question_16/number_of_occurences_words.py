# To count the number of occurences of words in a given string
def new_string(s):
    list1 = s.split(" ")
    dict1 = {}
    for i in list1:
        if(i in dict1):
            dict1[i] += 1
        else:
            dict1[i] = 1
    return dict1

user_input = input("Enter any string:")
result = new_string(user_input)
for i,j in result.items():
    print(f"{i} : {j}")
