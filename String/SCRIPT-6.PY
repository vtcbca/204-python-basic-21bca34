# write a script to enter any number and check number is palindrom or not.
a=int(input("Enter any number:"))
c=a
s=0
while(a>0):
    r=a%10
    s=r+s*10
    a=a//10
if(c==s):
    print("number is palindrom")
else:
    print("number is not palindrom")
