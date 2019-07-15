n=int(input("enter number of elements in list: "))
l=[]
for i in range(n):
    element=int(input())
    l.append(element)
print(l)
def minlist(l):
    m=min(l)
    print("smallest number in list: ",m)
minlist(l)
