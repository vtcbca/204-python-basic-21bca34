#wap script to enter any number and print the series in reverse.
a=int(input("enter any number:"))
b=0
while(a>0):
    c=a%10
    b=b*10+c
    a=a//10
print("the reverse number is:",b)    
