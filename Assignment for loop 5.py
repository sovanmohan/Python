x=int(input("enter the number for evaluation"))
n=int(input("enter the range"))
s=0
r=x
for i in range(1,n+1):
    s=s+r
    r=r+(10**i*x)
print(s)
