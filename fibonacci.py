n=int(input("enter the number of terms in fibonacci series: "))
print("the fibonacci series is: ")
t1=0
t2=1
for i in range(0,n):
    print(t1)
    t3=t2+t1
    t1=t2
    t2=t3
    
