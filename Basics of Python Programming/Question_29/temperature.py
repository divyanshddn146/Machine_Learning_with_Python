temperature = float(input("Enter your body temperture(°C):"))
if(temperature<97.8):
    print("Below body temperature")
elif(temperature>=97.8 and temperature<=99.1):
    print("Normal Body Temperature")
elif(temperature>99.1 and temperature<=100.3):
    print("Low Fever")
else:
    print("High Fever")
