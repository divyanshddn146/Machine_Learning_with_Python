user_input = input("Enter the type of car(s for sedan,p for prime,m for mini):")
user_input =user_input.lower()
distance = float(input("Enter the distance(in Km):"))
if(user_input == 's'):
    price = distance*17
    print(f"Total price is {price}")
elif(user_input == 'p'):
    price = distance*12
    print(f"Total price is {price}")
elif(user_input == 'm'):
    price = distance*10
    print(f"Total price is {price}")
else:
    print("Invalid Value")

