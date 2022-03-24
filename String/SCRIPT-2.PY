 # wap script to enter any number and print it is sum of digit.
a=int(input("enter number:"))
sum=0
while(a!=0):
    sum=sum+a%10
    a=a//10
    print("SUM OF IT:"),sum)
