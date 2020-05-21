import shapes
import base
xy = [0,0]

triangle = shapes.Triangle(xy,1,4)
circle = shapes.Circle(xy,2)
square = shapes.Square(xy,1)
ellipse = shapes.Ellipse(xy,3,2)
rectangle = shapes.Rectangle(xy,14,3)

mylist = [triangle,square,rectangle,circle,ellipse]

for item in mylist:
    if isinstance(item,base.Polygon):
        print(f"{item} located at {item.center} of size {item._size}")
    else:
        print(f"{item} located at {item.center} of radius {item.radius}")

