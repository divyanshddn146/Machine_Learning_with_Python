# To check whwether number is divisible by 10 or not
user_input = int(input("Enter the number:"))
if (user_input%10==0):
    print(f"Number {user_input} is divisible by 10")
else:
    print(f"Number {user_input} is not divisible by 10 so {user_input%10} should be added to make it divisible by 10")
