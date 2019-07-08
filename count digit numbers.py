n=input("enter a string: ")
alpha=num=0
for i in range(len(n)):
    if(n[i].isalpha()):
        alpha+=1
    elif(n[i].isdigit()):
        num+=1
print("letters= ",alpha)
print("digits= ",num)
