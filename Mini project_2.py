n=float(input("Enter a decimal number"))
rev=0
b=''
while(n!=0):
    d=int(n%2)
    b=str(d)+b
    n=n//2
print(b)
