
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import calculator

class UnitTestOfCalculator(unittest.TestCase):

    def setUp(self): 
        #このメソッドは，テストごとに事前に実行される
        # setUp() -> testInputNumber() -> setUp() -> testInput() -> … のように
        calculator.clear()

    def inputNumberSequence(self, key_sequence):
        for key in key_sequence:
            calculator.inputNumber(key)
        
   #inputNumberの単体テスト
    def testInputNumber(self):
        self.inputNumberSequence("012")
        self.assertAlmostEqual(calculator.inputValue, 12)
        
        self.inputNumberSequence("3456789")
        self.assertAlmostEqual(calculator.inputValue, 123456789)
        
    #inputの単体テスト
    def testInput(self):
        calculator.input("1")
        self.assertEqual(calculator.inputValue, 1)
        self.assertNotEqual(calculator.operation, "1")
        
        calculator.input("+")
        self.assertEqual(calculator.operation, "+")
        
        calculator.input("c")
        self.assertEqual(calculator.inputValue, 0)
        self.assertEqual(calculator.computation, 0)
        self.assertEqual(calculator.operation, "a")

    #factorialの単体テスト
    def testFact(self):
        self.assertEqual(calculator.fact(1), 1)
        self.assertEqual(calculator.fact(2), 2)
        self.assertEqual(calculator.fact(3), 3*2)
        self.assertEqual(calculator.fact(4), 4*3*2)
        self.assertEqual(calculator.fact(5), 5*4*3*2)

    #calculateの単体テスト
    #可能な限り他の関数の機能に依存しないようなコードを書く
    #そのため，input関数を使わず，直接値を代入している．
    def testCalculate(self):
        #test assign
        calculator.inputValue = 12
        calculator.operation = "a"
        calculator.calculate()
        self.assertEqual(calculator.computation, 12)

        #test plus
        calculator.inputValue = 23
        calculator.operation = "+"
        calculator.calculate()
        self.assertEqual(calculator.computation, 35)
        
        #test minus
        calculator.inputValue = 20
        calculator.operation = "-"
        calculator.calculate()
        self.assertEqual(calculator.computation, 15)

        #test multiply
        calculator.inputValue = 10
        calculator.operation = "*"
        calculator.calculate()
        self.assertEqual(calculator.computation, 150)
        
  
if __name__ == "__main__":
    unittest.main()


 
