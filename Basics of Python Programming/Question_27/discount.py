# To calculate discount 
user_input = float(input("Enter the amount to be paid:"))

if(user_input>=30000):
    discount = 30
elif(user_input>=20000):
    discount = 20
elif(user_input>=10000):
    discount = 10
else:
    discount = 5

amount = user_input - (discount/100)*user_input
print("Amount to be paid by custmer is %.2f"%amount)
