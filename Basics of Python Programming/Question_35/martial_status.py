user_input = input("Enter your martial status('S' for Separated,'M' for Married,'D' for Divorced,'U' for Unmarried):")
user_input = user_input.lower()
if(user_input == 'm'):
    print("Martial Status is Married")
elif(user_input == 's'):
    print("Martial Status is Seperated")
elif(user_input == 'd'):
    print("Martial Statuis is Divorced")
elif(user_input == 'u'):
    print("Martial Status is Unmarried")
else:
    print("Invalid Value entered")
