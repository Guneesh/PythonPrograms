for i in range(7):
    for j in range(5):
        if (((i>0 and i<7) and (j==0 or j==4)) or((j>0 and j<4)and (i==0 or i==3))):
            print("*",end="")
        else:
            print(end=" ")
    print()
