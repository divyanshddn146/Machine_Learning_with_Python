for i in range(5):
    print("")
    if(i<=2):
        for k in range(i+1):
            print("*",end=" ")
    else:
        for k in range(i%2+1):
            print("*",end=" ")

