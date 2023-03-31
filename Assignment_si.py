p=float(input("give principal"))
r=float(input("give rate of interest"))
n=int(input("give time"))
t=0
while(t<n):
    p=p+(p*r)/100.0
    print("amount",p)
    t+=1
