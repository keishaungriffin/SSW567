# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""
import sys
import unittest
from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(4,5,3),'Right','4,5,3 is a Right triangle') 

    def testIsocelesA(self): 
        self.assertEqual(classifyTriangle(5,5,10),'Isoceles','5,5,10 is an Isoceles triangle') 
        
    def testIsocelesB(self): 
        self.assertEqual(classifyTriangle(10,5,5),'Isoceles','10,5,5 is an Isoceles triangle')  
        
    def testIsocelesC(self): 
        self.assertEqual(classifyTriangle(5,10,5),'Isoceles','5,10,5 is an Isoceles triangle') 
        
    def testEquilateralTrianglesA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        
    def testEquilateralTrianglesB(self): 
        self.assertEqual(classifyTriangle(5,5,5),'Equilateral','1,1,1 should be equilateral')
        
    def testEquilateralTrianglesC(self): 
        self.assertEqual(classifyTriangle(10,10,10),'Equilateral','1,1,1 should be equilateral')
        
    def testScaleneTrianglesA(self): 
        self.assertEqual(classifyTriangle(6,7,9),'Scalene','6,7,9 should be scalene')
        
    def testScaleneTrianglesB(self): 
        self.assertEqual(classifyTriangle(5,7,9),'Scalene','5,7,9 should be scalene')
        
    def testScaleneTrianglesC(self): 
        self.assertEqual(classifyTriangle(2,3,5),'Scalene','2,3,5 should be scalene')
        
    def testIsvalidA(self): 
        self.assertEqual(classifyTriangle(0,0,0),'InvalidInput','0,0,0 is Invalid')
        
    def testIsvalidB(self): 
        self.assertEqual(classifyTriangle(201,200,203),'InvalidInput','201,200,203 is Invalid') 
        
    def testIsvalidC(self): 
        self.assertEqual(classifyTriangle(0,200,500),'InvalidInput','0,200,500 is Invalid')            

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
    
    
"""
#Output Testing results to txt file    
def main(out = sys.stderr, verbosity = 2):
    loader = unittest.TestLoader()
  
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out, verbosity = verbosity).run(suite)
      
if __name__ == '__main__':
    with open('testing.txt', 'w') as f:
        main(f)
"""
