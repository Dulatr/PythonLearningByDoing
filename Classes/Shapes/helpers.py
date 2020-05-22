"""
A collection of helper functions for the Shapes module.
"""
from math import pi,acos

def checkInput2D(values):
        """
        Checks an input for type (list,tuple), and checks elements in either
        for (int,float). 
        
        Returns a boolean.
        """
        if isinstance(values, (list,tuple)):
            if len(values) > 2:
                return False
                
            check = []

            for item in values:
                check.append(isinstance(item,(int,float)))

            return all(check)
        else:
            return False

def checkProperty(value,single=False):
    """
    Checks an input for (int,float). Returns a boolean.
    
    If a list of arguments provided, checks each argument
    in list for type (int,float)
    """
    if isinstance(value,(tuple,list)) and not single:
        for item in value:
            if isinstance(item,(tuple,list)):
                raise Exception(f"Argument of type {type(item)} not allowed.")
            checkProperty(item)
        return
    if not isinstance(value,(int,float)):
        raise Exception("Property must be set to (int,float)")
    if value <= 0:
        raise Exception("Property can't be set <= 0")
    
def angle(a,b,c,Angle='C'):
    """
    Use the law of cosines to obtain an angle knowing three sides of a triangle.
    
    Angle returned is based on str arg passed and in radians.
    """
    if not triInequality(a,b,c):
        raise Exception("Side lengths do not meet the triangle inequality.")

    if Angle=='C' or Angle=='c':
        cos_c = (a**2 + b**2 - c**2) / (2.0 * a * b)
        return acos(cos_c) 
    elif Angle=='B' or Angle=='b':
        cos_b = (a**2 + c**2 - b**2) / (2.0 * a * c)
        return acos(cos_b) 
    elif Angle=='A' or Angle=='a':
        cos_a = (b**2 + c**2 - a**2) / (2.0 * b * c)     
        return acos(cos_a)
    else:
        if isinstance(Angle,str):
            raise Exception("Invalid angle argument, must be A, B, or C")
        else:
            raise TypeError(f"Invalid type {type(Angle)} for argument Angle. Expected {type(str)}")

def triInequality(a,b,c):
    """
    Determines the triangle inequality for three provided sides of a triangle.

    Returns a Boolean if conditions are met.
    """
    args = [a,b,c]
    condition = []
    total = sum(args)
    
    for i in range(0,3):
        condition.append((total - args[i]) > args[i])
    
    return all(condition)
