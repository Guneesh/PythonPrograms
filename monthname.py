a=input("enter the month to find out the number of days: ")
if a=='January' or a=='March' or a=='May' or a=='July' or a=='August' or a=='October' or a=='December':
    print("number of days:31")
elif a=='April' or a=='June' or a=='September' or a== 'November':
    print("number of days:30")
elif a=='February':
    print("28/29 days")
else:
    print("enter a valid month")
