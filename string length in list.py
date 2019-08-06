n=int(input("enter the max length of string:"))
l1=['guneesh','dua','ab','yolo','whatever']
l2=[]
for i in l1:
    if len(i)>3:
        l2.append(i)
print(l2)
