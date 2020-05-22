# Shapes 

A basic module to learn the basics of inheritance within python. Shapes contains a list of basic objects that inherit from abstract classes `Shape` and `Polygon`. Shapes have a **location** and **size** property and can display the area and perimeter of itself through methods. Size is arbitrary and is really determined by the inheriting shape. So if there's more than one defining characteristic of the shape, it will return a tuple of those characteristics.

The current available shapes are:

* Square
* Circle
* Triangle
* Rectangle
* Ellipse 
* Rhombus
* Trapezoid

Each overriding their parent area and perimeter function. The location property checks for `(int,float)`inside of a `(list,tuple)` and raises an exception for the user otherwise.

## Usage

To use this module, add the folder to your local program directory and use imports:
```python
# predefined shapes
import shapes

# base classes: shape, polygon
import base

xy = [0,0]

circle = shapes.Circle(xy,2)
```
The [example.py](example.py) file contains an example of checking for types and property accessing for the different shapes.

