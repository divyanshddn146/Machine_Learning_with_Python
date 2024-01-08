# To input Weight in Kg
a=float(input("Enter your weight(in Kg):"))
# To input Height in meters
b=float(input("Enter your height(in meters):"))
# Formula for calculating BMI index
d=a/(b*b)
# Rounding off the result
c=round(d)
# Conditions for BMI index that are also listed in README file.
if(c<=18.5):
    print(f"Your BMI is {c} and you are underweight")
elif(c<25):
    print(f"Your BMI is {c} and you have a normal weight")
elif(c<30):
    print(f"Your BMI is {c} and you are slightly overweight")
elif(c<35):
    print(f"Your BMI is {c} and you are obese")
else:
    print(f"Your BMI is {c} and you are clinically obese")
