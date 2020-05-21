"""
A collection of defined basic geometric shapes.
"""
import base
from math import pi,sqrt
import helpers as h

class Circle(base.Shape):
    """
    A class defining a circle. Has attributes of center and radius. 
    User can query the area and perimeter.
    """
    def __init__(self,center,radius):
        if h.checkInput2D(center):
            super().__init__(center,radius)
        else:
            raise Exception("Location specified must be a list or tuple of int/float")

    def __str__(self):
        return "Circle"

    def area(self):
        return pi * self._size ** 2
    def perimeter(self):
        return 2 * pi * self._size   
    
    @property
    def radius(self):
        return self._size
    @radius.setter
    def radius(self,val):
        self._size = val

class Ellipse(Circle):
    """
    A circular object of varying radii. Has a major and minor axis.
    Inherits from shape, defines size as a tuple of radii.
    """
    def __init__(self,location,r_major,r_minor):
        if r_minor > r_major:
            raise Exception("Major axis must be greater than minor.")
        if h.checkInput2D(location):
            super().__init__(location,(r_major,r_minor))
        else:
            raise Exception("Location specified must be a list or tuple of int/float")

        self._major = r_major
        self._minor = r_minor

    def area(self):
        return self._minor * self._minor * pi
    def perimeter(self):
        """ 
        An approximation of the elliptical perimeter.
        Currently not implemented.
        """
        pass
    def __str__(self):
        return "Ellipse"
    @property
    def r_major(self):
        return self._major
    @r_major.setter
    def r_major(self,val):
        if isinstance(val,int):
            self._major = val
        else:
            raise Exception("Radius specified must be of type int")
    @property
    def r_minor(self):
        return self._minor
    @r_minor.setter
    def r_minor(self):
        if isinstance(val,int):
            self._minor = val
        else:
            raise Exception("Radius specified must be of type int")
    @property
    def e(self):
        return sqrt(1-(self._minor/self._major)**2)

class Square(base.Polygon):
    """
    A Polygon of edges 4, each of equal length.
    Size provided is the length of an edge from a corner.
    """
    def __init__(self,location,size):
        if h.checkInput2D(location):
            super().__init__(location,size,4)
        else:
            raise Exception("Location specified must be a list or tuple of int/float")
    
    def area(self):
        return self._size ** 2
    def perimeter(self):
        return 4 * self._size

    def __str__(self):
        return "Square"

class Triangle(base.Polygon):
    def __init__(self,location,base,height):
        if h.checkInput2D(location):
            super().__init__(location,(base,height),3)
        else:
            raise Exception("Location specified must be a list or tuple of int/float")
        self._base = base
        self._height = height

    def area(self):
        return 0.5 * self._base * self._height
    def perimeter(self):
        pass

    def __str__(self):
        return "Triangle"
    
    @property
    def base(self):
        return self._base
    @base.setter
    def base(self,val):
        self._base = val
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,val):
        self._height = val

class Rectangle(base.Polygon):
    """
    A polygon of 4 sides defined by base and height.
    Size is a tuple of (base,height).
    """
    def __init__(self,location,base,height):
        if h.checkInput2D(location):
            super().__init__(location,(base,height),4)
        else:
            raise Exception("Location specified must be a list or tuple of int/float")
        self._base = base
        self._height = height
    
    def area(self):
        return self._height * self._base
    def perimeter(self):
        return self._height * 2 + self._base * 2

    def __str__(self):
        return "Rectangle"
    
    @property
    def base(self):
        return self._base
    @base.setter
    def base(self,val):
        self._base = val
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,val):
        self._height = val

class Rhombus(base.Polygon):
    """
    Currently not implemented
    """
    pass

class Trapezoid(base.Polygon):
    """
    Currently not implemented
    """
    pass

class Parallelogram(base.Polygon):
    """
    Currently not implemented
    """
    pass