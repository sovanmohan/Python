n=int(input("Enter a number"))
c=0
while(n!=0):
    d=n%10
    c+=1
    n=n//10
print("Number of digits in the given number",c)
