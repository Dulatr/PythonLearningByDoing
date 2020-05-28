"""
A collection of methods for calculating the distance between two points on the surface of a sphere.
"""
from math import asin,cos,sin,sqrt,pi

def distance(points,r):
    """
    Returns the absolute distance between to points on a sphere.
    """
    return 2.0 * r * arcHav(func(points))

def func(points):
    """
    The Haversine formula for two points
    """
    city1 = (points[0][0]*pi/180, points[0][1]*pi/180)
    city2 = (points[1][0]*pi/180, points[1][1]*pi/180)  

    return hav(city2[0] - city1[0]) + cos(city1[0]) * cos(city2[0]) * hav(city2[1] - city1[1])

def hav(theta):
    """
    The Haversine function
    """
    return (1.0 - cos(theta)) / 2.0

def arcHav(h):
    """
    Inverse haversine

    If value passed isn't between 0 and 1, raises ValueError.
    """
    if h > 1 or h < 0:
        raise ValueError("Haversine value must be between 0 and 1")
    return asin(sqrt(h))