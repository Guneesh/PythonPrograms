n=int(input("enter the number of elements of first list: "))
l1=[]
for i in range(n):
    e1=(input())
    l1.append(e1)
print(l1)
m=int(input("enter the number of elements of second list: "))
l2=[]
for j in range(m):
    e2=(input())
    l2.append(e2)
print(l2)
l1.extend(l2)
print("concatenation will give the result: ",l1)
