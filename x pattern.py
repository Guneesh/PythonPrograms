for i in range(7):
    for j in range(6):
        if (((j==0 or j==5) and (i==0 or i==1 or i==5 or i==6)) or ((j==1 or j==4) and (i==2 or i==4)) or (i==3 and j==2)):
            print("*",end="")
        else:
            print(end=" ")
    print()
