import unittest
from CalculatorClass import Calculator

class TestCalculator(unittest.TestCase):

    def test_sum(self):
        calc = Calculator()
        self.assertEqual(calc.sum(1,1), 2)

    def test_minus(self):
        calc = Calculator()
        self.assertEqual(calc.minus(1,1),0)
    
    def test_product(self):
        calc = Calculator()
        self.assertEqual(calc.product(1,1),1)

    def test_dividen(self):
        calc = Calculator()