s=input("enter a string: ")
count=0
for i in range(len(s)):
    if s[i]=='e' or s[i]=='a'or s[i]=='i'or s[i]=='o' or s[i]=='u':
        count+=1

print("number of vowels is ",count)
