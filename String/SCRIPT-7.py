# write a script to enter any number and print it is prime number or not.
a=int(input("Enter any number"))
i=2
no=0
for i in range(2,a):
    if(a%i==0):
        c=1
        break
        i=i+1
    if(a==1):
        print("This is not a prime number")
    else:
        print("this is a prime number")
