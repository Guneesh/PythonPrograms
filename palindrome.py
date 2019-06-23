n=int(input("enter an integer:"))
org=n
rev=0
while(n>0):
  rem=n%10
  rev=(rev*10)+rem
  n=n//10
if org==rev:
    print("the given number is a palindrome!")
else:
    print("the givn number is not a palindrome!")
