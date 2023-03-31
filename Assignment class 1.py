class circle:
    def __init__ (circ,radius):
        circ.radius=radius
    def area(circ):
        print("Area",(3.14*circ.radius**2))
    def circumference(circ):
         print("Circumference",(2*3.14*circ.radius))
t=float(input("enter the radius"))
p1=circle(t)
p1.area()
p1.circumference()
        
