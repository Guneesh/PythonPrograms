n=int(input("enter number of elements in list: "))
l=[]
for i in range(n):
    element=int(input())
    l.append(element)
print("original list: ",l)
duplicate= set()
unique=[]
for item in l:
    if item not in duplicate:
        unique.append(item)
        duplicate.add(item)

print("list after removing duplicates: ",unique)
        
