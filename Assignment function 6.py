def prime(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c+=1
    if(c==2):
        return 1
    else:
        return 0
n=int(input("Enter a number"))
t=prime(n)
if(t==1):
    print("prime")
else:
    print("not prime")
