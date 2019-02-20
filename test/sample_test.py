
import unittest

def plus(x,y):
	return x+y

def minus(x,y):
	return x*y

class Tester(unittest.TestCase):
	def testPlus(self):
		self.assertEqual(plus(3,2),5)  # 3 + 2 = 5
		self.assertEqual(plus(10,20),30) # 10 + 20 = 30
		#self.assertAlomstEqual(plus(0.2,0.3),0.5) # 0.2 + 0.3 = 0.5

	def testMinus(self):
		self.assertEqual(minus(3,2),6)
	
if __name__ == "__main__":
	unittest.main()
				
