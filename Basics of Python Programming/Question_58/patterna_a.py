for i in range(5):
    print("")
    for j in range(5):
        if((i+j==2 or i+j==4 or i+j==6) ):
            if(((i==4 and j == 0) or (i==0 and j==4))):
                print(" ", end=" ")
            else:
                print("*",end = " ")
        else:
            print(" ",end = " ")

