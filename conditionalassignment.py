n=int(input("enter a number between 1500 and 2700: "))
if n>=1500 and n<=2700:
    if n%7==0 and n%5==0:
        print("the number is divisible by 7 and a multiple of 5")
    else:
        print("the number dosen't satisfy the condition")
else:
    print("invalid input")
