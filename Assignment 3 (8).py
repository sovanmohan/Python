n=int(input("Enter a number"))
p=n
rev=0
while(n!=0):
    d=n%10
    rev=rev*10+d
    n=n//10
if(p==rev):
    print("Palindrome")
else:
    print("not palindrome")
    
