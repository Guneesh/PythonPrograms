n=int(input("enter the length of list: "))
l=[]
count=0
for i in range(n):
    element=input()
    l.append(element)
print(l)
for j in l:
    if len(j)>1 and j[0]==j[-1]:
        count+=1
    
print("answer is: ",count)
    
