for i in range(5):
    print("")
    for j in range(5):
        if(i==j or i+j==4):
            print("$",end = " ")
        elif(j==0 or j ==4 or i == 0 or i==4):
             print("*",end = " ")
        else:
            print(" ",end = " ")

