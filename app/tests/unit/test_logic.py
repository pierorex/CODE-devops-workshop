from unittest import TestCase

from calculator.app import app
from calculator.logic import Calculator

from calculator.logic import ValueTooLowException, ValueTooHighException


class CalculatorTests(TestCase):
    def test_mul(self):
        calc = Calculator(-100000, 100000)
        self.assertEqual(calc.mul(1, 1), 1)
        self.assertEqual(calc.mul(1, 0), 0)
        self.assertEqual(calc.mul(0, 1), 0)
        self.assertEqual(calc.mul(100, 10), 1000)
        self.assertEqual(calc.mul(1, 1), 1)

    def test_boundaries(self):
        calc = Calculator(-100, 100)
        self.assertRaises(ValueTooLowException, lambda: calc.div(-101, 1))
        self.assertRaises(ValueTooHighException, lambda: calc.mul(101, 1))


    def test_valid(self):
        calc = Calculator(-100000, 100000)
        self.assertRaises(ValueTooLowException, lambda: calc.div(-100000000000, 1))
        self.assertRaises(ValueTooHighException, lambda: calc.div(100000000000, 1))
        self.assertRaises(ValueTooLowException, lambda: calc.div(1, -100000000000))
        self.assertRaises(ValueTooHighException, lambda: calc.div(1, 100000000000))

    def test_div(self):
        calc = Calculator(-100000, 100000)
        self.assertEqual(calc.div(1, 1), 1)
        self.assertEqual(calc.div(0, 1), 0)
        self.assertEqual(calc.div(100, 10), 10)
        self.assertEqual(calc.div(1, 1), 1)
        self.assertRaises(ZeroDivisionError, lambda: calc.div(1, 0))

    def test_invalid_http_request(self):
        self.app = app.test_client()
        response = self.app.get('/calc/10/0')
        self.assertEqual(response.status_code, '403')
