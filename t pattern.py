for i in range(5):
    for j in range(5):
        if (j==2 or (i==0 and j!=2)):
            print("*",end="")
        else:
            print(end=" ")
    print()
