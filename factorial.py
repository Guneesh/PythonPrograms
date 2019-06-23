n=int(input("enter an integer: "))
if n<0:
    print("factorial can't be determined!!")
elif n==0:
    print("factorial is 1")
else:
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print("factorial of ",n," is ",fact)
