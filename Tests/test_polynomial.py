from Polynomial import Polynomial, Point
import unittest
import numpy as np


class TestInitializer(unittest.TestCase):

    def setUp(self) -> None:
        self.poly = Polynomial(Point(1, 29), Point(-1, -35), Point(2, 31), Point(-3, -19))

    def test_polynomial_init(self):
        self.assertEqual(self.poly.degree, 3)
        self.assertListEqual([int(x) for x in self.poly.coeffs], [-4, -2, 36, -1])


class TestMethods(unittest.TestCase):

    def setUp(self) -> None:
        self.poly1 = Polynomial(Point(1, 29), Point(-1, -35), Point(2, 31), Point(-3, -19))
        self.poly1Duplicate = Polynomial(Point(1, 29), Point(-1, -35), Point(2, 31), Point(-3, -19))
        self.poly1Derivative = Polynomial(coeffs=[-12, -4, 36])
        self.poly1Integral = Polynomial(coeffs=[-1,-2/3, 18, -1, 'C'])

    def test_equals(self):
        self.assertEqual(self.poly1, self.poly1Duplicate)

    def test_integral(self):
        self.assertEqual(self.poly1Integral, self.poly1.get_integral())

    def test_derivative(self):
        self.assertEqual(self.poly1Derivative, self.poly1.get_derivative())

    def test_coefficients(self):
        pass

    def test_evaluate(self):
        self.poly1 = Polynomial(Point(1, 29), Point(-1, -35), Point(2, 31), Point(-3, -19))
        x = [-10, 0, 1, 10, 17, 20]
        vX = np.array(x)
        y = [3439, -1, 29, -3841, -19619, -32081]
        vY = np.array(y)

        for (i, xVal) in enumerate(x):
            self.assertEqual(y[i], int(self.poly1.evaluate(xVal)))

        for (i, yVal) in enumerate(self.poly1.evaluate(vX)):
            self.assertAlmostEqual(yVal, vY[i])


if __name__ == '__main__':
    unittest.main()
