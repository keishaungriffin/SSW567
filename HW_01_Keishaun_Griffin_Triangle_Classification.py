import unittest 

# Function check the classification of triangle 
def classify_triangle(a,b,c):
    if a==b and b==c:
        return('Equilateral')
    elif a==b or b==c or a==c:
        return('Isosceles')
    elif a!=b or b!=c or a!=c:
        return('Scalene')
    
def is_right(a,b,c):
    if a*a+b*b==c*c or b*b+c*c==a*a or c*c+a*a==b*b:
        return('Right')
    else:
        return False


class TestTriangles(unittest.TestCase):
    
    def test_MyTestSet1(self): 
        self.assertEqual(is_right(6,8,10),'Right','Should be Right')
        self.assertEqual(is_right(3,4,5),'Right','Should be Right')

        
    def test_MyTestSet2(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertEqual(classify_triangle(10,10,10),'Equilateral','Should be Equilateral')
        self.assertEqual(classify_triangle(10,15,30),'Scalene','Should be Scalene')
        self.assertEqual(classify_triangle(7,9,30),'Scalene','Should be Scalene')
        self.assertEqual(classify_triangle(5,5,10),'Isosceles','Should be Isosceles')
        self.assertEqual(classify_triangle(10,10,2),'Isosceles','Should be Isosceles')

        
        

if __name__ == '__main__':
    # examples of running the code
    classify_triangle(10,10,10)
    classify_triangle(6,8,10)
    classify_triangle(5,5,10)
    classify_triangle(7,9,30)
    is_right(3,4,5,)
    is_right(6,8,10)
    
    unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder