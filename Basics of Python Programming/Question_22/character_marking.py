user_input = input("Enter character A,B,C,D or E:")
if(user_input=="A" or user_input=="B" or user_input=="C" or user_input=="D" or user_input=="E"):
    if(user_input=="A"):
        print("Outstanding")
    elif(user_input == "B"):
        print("Very Good")
    elif(user_input == "C"):
        print("Good")
    elif(user_input == "D"):
        print("Average")
    else:
        print("Fail")
else:
    print("Wrong value entered")
