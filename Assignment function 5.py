def mul(l):
    t=1
    for i in range(len(l)):
        t=t*l[i]
    return t
n=int(input("Enter how many numbers you want in the list"))
l=[]
for i in range(n):
    x=int(input("Enter the number"))
    l.append(x)
print(mul(l))
