def perfect(n):
    if(n>=0):
        s=0
        for i in range(1,n):
            if(n%i==0):
                s=s+i
        if(s==n):
            return 1
        else:
            return 0
    else:
        print("Invalid input")
n=int(input("enter a number"))
if(perfect(n)==1):
    print("Perfect number")
else:
    print("not a perfect number")
