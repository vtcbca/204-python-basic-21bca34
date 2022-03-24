# wap a script to enter any number and check number is armstrong is not.
a=int(input("Enter any number:"))
d=a
c=0
while(a>0):
    b=a%10
    c=c+b*b*b
    a=a//10
if(d==c):
    print(" it is an armstrong number")
else:
    print(" it is not a armstrong number")



