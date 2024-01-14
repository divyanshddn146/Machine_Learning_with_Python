def max_len():
    print("Enter a list of string(q to quit):")
    list_string = []
    while(True):
        user_input = input()
        if(user_input.lower()=='q'):
            break
        list_string.append(user_input)

    max = list_string[0]
    for i in range(1,len(list_string)):

        if(len(list_string[i]) > len(max)):
            max = list_string[i]
    return len(max)

result = max_len()
print(f"Maximum length word is {result}")
