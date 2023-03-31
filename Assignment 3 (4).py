def outer(a,b):
    def inner():
        r=a+b
        return r
    r=inner()+5
    return r
a=int(input("Enter the number"))
b=int(input("Enter the number"))
print(outer(a,b))

