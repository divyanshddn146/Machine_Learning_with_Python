import math

length = float(input("Enter the length of rectangle:"))
breath = float(input("Enter the breath of rectangle:"))
while(True):
    user_input = input('''
    Enter 1 to calculate perimeter
    Enter 2 to calculte area
    Enter 3 to calculate diagonal
    Enter q to quit the program
    ''')
    if(user_input=="1"):
        perimeter = 2*(length+breath)
        print(f"Perimeter of Rectangle is {perimeter}")
    elif(user_input=="2"):
        area = length*breath
        print(f"The area of rectangle is {area}")
    elif(user_input == "3"):
        diagonal = math.sqrt(l**2+b**2)
        print(f"The diagonal of rectagle is {diagonal}")
    elif(user_input == "q" or user_input == "Q"):
        break
    else:
        print("Wrong Input")
        print("Pls try again or enter q to quit.")
