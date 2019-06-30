print("1.farhenheit to celsius")
print("2.celsius to farhenheit")
n=int(input("enter your choice: "))
if n==1:
    m=int(input("enter temparature in farhenheit: "))
    o=(m-32)/1.8
    print("temparature in celcius: ",o)
elif n==2:
    p=int(input("enter temparature in celcius: "))
    q=1.8*p+32
    print("temparature in farhenheit: ",q)
    
    
