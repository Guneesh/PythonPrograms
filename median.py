a=int(input("enter the first integer: "))
b=int(input("enter the second integer: "))
c=int(input("enter the third integer: "))
median=0
if a>b:
    if a<c:
        median=a
    elif b>c:
        median=b
    else:
        median=c
else:
    if b<c:
        median=b
    elif a>c:
        median=a
    else:
        mdian=c
print("median is: ",median)
