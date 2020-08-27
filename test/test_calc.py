import unittest

from pycode.calc import Calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.calc = Calc()
        result = self.calc.add(1,2)
        self.assertEqual(result,3)
        print(result)