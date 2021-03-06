"""
A collection of defined basic geometric shapes.
"""
import base
from math import pi,sqrt,sin
import helpers as h
from warnings import warn

class Circle(base.Shape):
    """
    A class defining a circle. Has attributes of center and radius. 
    User can query the area and perimeter.
    """
    def __init__(self,center,radius):
        if h.checkInput2D(center):
            if isinstance(radius,(float,int)):
                super().__init__(center,radius)
            else:
                raise Exception(f"Cannot create radius of type {type(radius)}")
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
        h.checkProperty(val)
        self._size = val

class Ellipse(Circle):
    """
    A circular object of varying radii. Has a major and minor axis.
    Inherits from shape, defines size as a tuple of radii.
    """
    def __init__(self,location,r_major,r_minor):
        h.checkProperty([r_major,r_minor])
        if r_minor > r_major:
            raise Exception("Major axis must be greater than or equal to minor.")
        if h.checkInput2D(location):
            super().__init__(location,r_major)
        else:
            raise Exception("Location specified must be a list or tuple of int/float")

        self._major = r_major
        self._minor = r_minor

    def area(self):
        return self._minor * self._minor * pi
    def perimeter(self):
        """
        Returns the perimeter approximation. If major is not aprox. 3 times larger than
        minor axis, approximation is reasonable. Else a warning is printed to the user. 
        """
        if self._major > 3.0 * self._minor:
            warn("Major axis is much larger than the minor axis. Perimeter error may be large.",Warning,stacklevel=2)
        return 2.0 * pi * sqrt((self._major ** 2 + self._minor ** 2) / 2.0)

    def __str__(self):
        return "Ellipse"

    @property
    def r_major(self):
        return self._major
    @r_major.setter
    def r_major(self,val):
        h.checkProperty(val)
        self._major = val
    @property
    def r_minor(self):
        return self._minor
    @r_minor.setter
    def r_minor(self,val):
        h.checkProperty(val)
        self._minor = val

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
            if isinstance(size,(float,int)):
                super().__init__(location,size,4)
            else:
                raise Exception(f"Cannot create side length of type {type(size)}")
        else:
            raise Exception("Location specified must be a list or tuple of int/float")
    
    def area(self):
        return self._size ** 2
    def perimeter(self):
        return 4 * self._size

    def __str__(self):
        return "Square"

class Triangle(base.Polygon):
    """
    A 3 sided polygon with height perpindicular to the base. 

    Side args start on the right and work counterclockwise.
    <side_c> is the base.
    """
    def __init__(self,location,side_a,side_b,side_c):
        if h.checkInput2D(location):
            h.checkProperty([side_a,side_b,side_c])
            super().__init__(location,(side_a,side_b,side_c),3)
        else:
            raise Exception("Location specified must be a list or tuple of int/float")
        self._side_a = side_a
        self._side_b = side_b
        self._base = side_c
        self._height = sin(h.angle(side_a,side_b,side_c,Angle='A')) * side_b

    def area(self):
        return 0.5 * self._base * self._height
    def perimeter(self):
        return self._side_a + self._side_b + self._base 

    def __str__(self):
        return "Triangle"
    
    @property
    def a(self):
        return self._side_a
    @a.setter
    def a(self,val):
        h.checkProperty(val,True)
        self._side_a = val        
        self._height = sin(h.angle(self._side_a,self._side_b,self._base,Angle='A')) * self._side_b
    @property
    def b(self):
        return self._side_b
    @b.setter
    def b(self,val):
        h.checkProperty(val,True)
        self._side_b = val        
        self._height = sin(h.angle(self._side_a,self._side_b,self._base,Angle='A')) * self._side_b
    @property
    def base(self):
        return self._base
    @base.setter
    def base(self,val):
        h.checkProperty(val,True)
        self._base = val        
        self._height = sin(h.angle(self._side_a,self._side_b,self._base,Angle='A')) * self._side_b
    @property
    def height(self):
        return self._height

class Rectangle(base.Polygon):
    """
    A polygon of 4 sides defined by base and height.
    Size is a tuple of (base,height).
    """
    def __init__(self,location,base,height):
        if h.checkInput2D(location):
            h.checkProperty([base,height])
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
        h.checkProperty(val)
        self._base = val
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,val):
        h.checkProperty(val)
        self._height = val

class Rhombus(base.Polygon):
    """
    A 4 sided polygon each of same length at angles less than 90 degrees to each other.
    """
    def __init__(self,location,diagonal_1,diagonal_2):
        if h.checkInput2D(location):
            h.checkProperty([diagonal_1,diagonal_2])            
            super().__init__(location,(diagonal_1,diagonal_2),4)        
        else:
            raise Exception("Location specified must be a list or tuple of int/float")
        
        self._d1 = diagonal_1
        self._d2 = diagonal_2
        self._a = sqrt((0.5 * self._d1) ** 2 + (0.5 * self._d2) ** 2)

        if not h.triInequality((0.5 * self._d1), (0.5 * self._d2), self._a):
            raise ValueError("Side lengths invalid, must follow triangle inequality.")
   
    def area(self):
        return self._d1 * self._d2 / 2.0
    def perimeter(self):     
        return 4.0 * self._a
    
    def __str__(self):
        return "Rhombus"

    @property
    def d1(self):
        return self._d1
    @d1.setter
    def d1(self,val):
        h.checkProperty(val)
        self._d1 = val
    @property
    def d2(self):
        return self._d2
    @d2.setter
    def d2(self,val):
        h.checkProperty(val)
        self._d2 = val
    @property
    def a(self):
        return self._a
    @a.setter
    def a(self,val):
        if not h.triInequality((0.5 * self._d1),(0.5 * self._d2),self._a):
            raise ValueError("Side length invalid, must follow triangle inequality.")
        h.checkProperty(val)
        self._a = val

class Trapezoid(Rectangle):
    """
    A 4 sided polygon with at least one set of parallel sides.
    """
    def __init__(self,location,base,height,side_a,side_c,side_d):
        if h.checkInput2D(location):
            super().__init__(location,base,height)
            h.checkProperty([side_a,side_c,side_d])            
        else:
            raise Exception("Location specified must be a list or tuple of int/float")

        self._side_a = side_a
        self._side_c = side_c
        self._side_d = side_d
    
    def area(self):
        return ((self._side_a + self._base) / 2.0) * self.height
    def perimeter(self):
        return self._side_a + self._base + self._side_c + self._side_d
    
    def __str__(self):
        return "Trapezoid"

    @property
    def A(self):
        return self._side_a
    @A.setter
    def A(self,val):
        h.checkProperty(val)
        self._side_a = val
    @property
    def C(self):
        return self._side_c
    @C.setter
    def C(self,val):
        h.checkProperty(val)
        self._side_c = val
    @property
    def D(self):
        return self._side_d
    @D.setter
    def D(self,val):
        h.checkProperty(val)
        self._side_d = val

     