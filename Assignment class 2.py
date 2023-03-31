class rectangle:
    def __init__ (t,length,breadth):
        t.length=length
        t.breadth=breadth
    def area(t):
        print("Area",(t.length*t.breadth))
    def perimeter(t):
         print("Perimeter",(2*t.length)+(2*t.breadth))
l=float(input("length"))
b=float(input("breadth"))
p1=rectangle(l,b)
p1.area()
p1.perimeter()
        
