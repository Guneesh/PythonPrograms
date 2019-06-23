n=int(input("enter the length of pattern:"))
temp=1
for i in range(n):
    for j in range(1,i+1):
       print(temp,end=" ")
       temp+=1
    print()
