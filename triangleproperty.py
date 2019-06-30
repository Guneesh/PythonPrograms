a=int(input("enter the first side of triangle: "))
b=int(input("enter the second side of triangle: "))
c=int(input("enter the third side of triangle: "))
if a==b and b==c:
    print("equilateral triangle !")
elif (a==b and b!=c) or (b==c and a!=c) or (a==c and b!=c):
    print("isoceless triangle !")
elif a!=b and b!=c:
    print("scalene triangle !")

