from Polynomial import Polynomial, Point
import unittest


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
        pass


if __name__ == '__main__':
    unittest.main()
