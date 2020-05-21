"""
Base object classes. Contains abstractions of geometric objects.
Use the shapes module instead.
"""

import abc

class Shape(abc.ABC):
    """
    An abstract class that defines an ambiguous shape of set size at set location.
    """
    @abc.abstractmethod
    def __init__(self,location,size):
        self._location = location
        self._size = size

    @abc.abstractmethod
    def area(self):
        """The area of the shape instance"""
        pass

    @abc.abstractmethod
    def perimeter(self):
        """The perimeter of the shape instance"""
        pass
    
    @property
    def center(self):
        return self._location
    @center.setter
    def center(self,val):
        if h.checkInput2D(val):
            self._location = val
        else:
            raise Exception("Location specified must be a list or tuple of int/float")
 
class Polygon(Shape):
    """
    An abstract class inherited from Shape. Has edges and vertices. 
    """
    def __init__(self,location,size,edges):
        super().__init__(location,size)
        if edges == 0:
            raise Exception("Cannot instantiate Polygon with edges 0.")
        self._edges = edges
    @property
    def vertices(self):
        return self._edges
    @property 
    def edges(self):
        return self._edges

class Polyhedra(Shape):
    """
    A class defining a 3-dimensional shape. 
    Currently not implemented.
    """
    pass    