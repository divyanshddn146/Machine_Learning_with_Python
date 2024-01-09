# To calculate total salary
salary = float(input("Enter your basic pay:"))
hra = .1*salary
ta = .05*salary
total = hra + ta + salary
print("Your total salary is %.2f"%(total))
