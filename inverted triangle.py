for i in range(9):
    for j in range(5):
        if (j==0 and (i>=0 and i<=8)) or (j==1 and (i>0 and i<8)) or (j==2 and (i>1 and i<7)) or (j==3 and (i>2 and i<6)) or (j==4 and i==4):
            print("*",end=" ")
        else:
            print(end=" ")
    print()
    
