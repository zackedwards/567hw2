# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classifyTriangle(a,b,c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """

    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if (isinstance(a,str) or isinstance(b,str) or isinstance(c,str)):
        if(isinstance(a, str)):
            if(a.isnumeric()):
                a = float(a)
            else:
                #must have valid numbers to continue
                return'InvalidInput'
        if(isinstance(b, str)):
            if(b.isnumeric()):
                b = float(b)
            else:
                return'InvalidInput'
        if(isinstance(c, str)):
            if(c.isnumeric()):
                c = float(c)
            else:
                return'InvalidInput'
    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
        
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
      
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # or the specified shape is not a triangle
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'
    mylist = [a, b, c]
    mylist.sort(key=None, reverse=True)
    # now we know that we have a valid triangle 
    if a == b and b == a and c==a:
        return 'Equilateral'
    elif ((mylist[2] ** 2) + (mylist[1] ** 2)) == (mylist[0] ** 2):
        return 'Right'
    elif (a != b) and  (b != c) and (a != c):
        return 'Scalene'
    else:
        return 'Isosceles'
