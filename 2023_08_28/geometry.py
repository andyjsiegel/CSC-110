'''
Andy Siegel
CSC 110
Project 1
This program has several functions which return the area of various shapes. 
'''

def rectangle_area(base, height):
    '''
    This function returns the rectangular area of its two parameters.
    Args:
        base: the base of the rectangle
        height: the height of the rectangle
    Returns:
        the area made up of the base and height of the rectangle
    '''
    area = base * height
    return area


def triangle_area(a, b, c):
    '''
    This function returns the rectangular area of its two parameters.
    Args:
        a: the first side of the triangle
        b: the second side of the triangle
        c: the third side of the triangle
    Returns:
        the area of the triangle by using the semi perimeter
    '''
    s = (a + b + c) / 2
    area = ( (s*(s-a)*(s-b)*(s-c)) ** (1/2) ) 
    return area 

def trapezoid_area(base_1, base_2, height):
    '''
    This function returns the trapezoidal area given two bases and a height. 
    Args:
        base_1: the first base of the trapezoid
        base_2: the second base of the trapezoid
        height: the height of the trapezoid
    Returns:
        the area of the trapezoid
    ''' 
    area = 0.5 * (base_1 + base_2) * height
    return area

def circle_area(radius):
    '''
    This function returns the area of a circle given its radius
    Args:
        radius: the radius of the circle
    Returns:
        the area of the circle
    '''
    area = round(3.1415 * (radius ** 2), 2)
    return area

