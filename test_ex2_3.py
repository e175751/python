import unittest
import ex2_3

class TestStringMethods(unittest.TestCase):
    
    def test_register(self):
    	self.asserEqual(6469.2,479.2,ex2_3.register(5990))
    	
if __name__=='__main__':
	unittest.main()
	    	
