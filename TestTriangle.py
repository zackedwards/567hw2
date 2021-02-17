# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightA(self): #Testing for right triangle detection
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
    def testRightB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
    def testRightC(self):
        self.assertEqual(classifyTriangle(5,12,13), "Right", "Should be a scalene, right triangle")
    def testRightD(self):
        self.assertEqual(classifyTriangle(6,8,10), "Right", "Should be a scalene, right triangle")
    def testRightE(self):
        self.assertEqual(classifyTriangle(12,35,37), "Right", "Should be a scalene, right triangle")
    def testRightF(self):
        self.assertNotEqual(classifyTriangle(3,4,6),'Right','3,4,6 is not a right scalene triangle')
        
    def testEquilateralA(self): #Testing for equilateral triangle detection
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    def testEquilateralB(self): 
        self.assertEqual(classifyTriangle(3,3,'3'),'Equilateral','1,1,1 should be equilateral')
    def testEquilateralC(self):
        self.assertEqual(classifyTriangle(27,27,27),'Equilateral','27,27,27 should be equilateral')
    def testEquilateralD(self):
        self.assertNotEqual(classifyTriangle(8,8,9),'Equilateral','8,8,9 should not be equilateral')
        
    def testNotATriangleA(self): 
        #Testing for scalene triangle detection
        self.assertEqual(classifyTriangle(4, 7, 87),'NotATriangle','Should be NotATriangle')
    def testNotATriangleB(self): 
        self.assertEqual(classifyTriangle(10,15,30),'NotATriangle','Should be NotATriangle')
    def testNotATriangleC(self): 
        self.assertEqual(classifyTriangle(1,88,9),'NotATriangle','Should be NotATriangle') 
    
    def testIsocelesA(self): #Testing for isoscles triangle detection
        self.assertEqual(classifyTriangle(10,10,15),'Isosceles','Should be isosceles')
    def testIsocelesB(self):
        self.assertEqual(classifyTriangle(4,6,4),'Isosceles','Should be isosceles')
    def testIsocelesC(self):
        self.assertNotEqual(classifyTriangle(10,10,10),'Isosceles','Should not be isosceles')
        
    def testInvalidA(self): #Testing for invalid entries such as words or negatives
        self.assertEqual(classifyTriangle("a",10,15),'InvalidInput','Should be invalid')
    def testInvalidB(self):
        self.assertEqual(classifyTriangle(5,10,'b'),'InvalidInput','Should be invalid')
    def testInvalidC(self):
        self.assertNotEqual(classifyTriangle("7",10,15),'InvalidInput','Should not be invalid')
    def testInvalidD(self):
        self.assertNotEqual(classifyTriangle('5','5','7'),'InvalidInput','Should not be invalid')
    def testInvalidE(self):
        self.assertEqual(classifyTriangle(5,10,'four'),'InvalidInput','Should be invalid')
    def testInvalidF(self):
        self.assertEqual(classifyTriangle(5,10,-9),'InvalidInput','Should be invalid')
        
    def testScaleneA(self): 
        self.assertEqual(classifyTriangle(9, 13, 14),'Scalene','Should be Scalene')
    def testScaleneB(self): 
        self.assertEqual(classifyTriangle(15, 32, 34),'Scalene','Should be Scalene')
    def testScaleneC(self): 
        self.assertEqual(classifyTriangle(2, 4, 5),'Scalene','Should be Scalene')
        
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

