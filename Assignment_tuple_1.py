tuple1=("disco","pop",10,1.2)
print(len(tuple1))
print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))
print(type(tuple1[3]))
print(tuple1[1:3])
x=list(tuple1)
x[0]="jazz"
tuple1=tuple(x)
print(tuple1)
tuple1=tuple1+("blue",)
print(tuple1)
x=list(tuple1)
x.remove(1.2)
tuple1=tuple(x)
print(tuple1)


