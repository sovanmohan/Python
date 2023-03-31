
def fibo(n):
    a=0
    b=1
    print(0)
    print(1)
    for i in range(n-2):
        c=a+b
        a=b
        b=c
        print(c)
fibo(10)
    
