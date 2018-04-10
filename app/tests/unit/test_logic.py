from unittest import TestCase
from app.calculator.logic import Calculator

from app.calculator.logic import ValueTooLowException, ValueTooHighException


class CalculatorTests(TestCase):
    def test_mul(self):
        calc = Calculator(-100000, 100000)
        assert (calc.mul(1, 1) == 1)
        assert (calc.mul(1, 0) == 0)
        assert (calc.mul(0, 1) == 0)
        assert (calc.mul(100, 10) == 1000)
        assert (calc.mul(1, 1) == 1)
        self.assertRaises(ValueTooLowException, lambda: calc.mul(-100000000000, 1))
        self.assertRaises(ValueTooHighException, lambda: calc.mul(100000000000, 1))
        self.assertRaises(ValueTooLowException, lambda: calc.mul(1, -100000000000))
        self.assertRaises(ValueTooHighException, lambda: calc.mul(1, 100000000000))

    def test_div(self):
        pass
