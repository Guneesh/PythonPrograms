import random
n=0
m=random.randint(1,10)
while n!=m:
    n=int(input("guess a number between 1 and 9: "))
    if n==m:
        print("well guessed!")
    else:
        print("try again!")
    

  
   
