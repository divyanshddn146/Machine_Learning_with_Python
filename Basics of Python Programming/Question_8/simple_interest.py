# To calculate simple interest

p = float(input("Enter the principal amount:"))
r = float(input("Enter the rate(in percent):"))
t = int(input("Enter the time period:"))
si = p*r*t/100
print("Simple interest is %.2f"%(si))

# To calculate compound interest

p = float(input("Enter the principal amount:"))
r = float(input("Enter the rate(in percent):"))
t = int(input("Enter the time period:"))

ci = (p*((1+r/100)**(t)))-p
print("Compound interest is %.2f"%(ci))
