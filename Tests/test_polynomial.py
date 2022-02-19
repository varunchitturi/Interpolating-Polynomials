from Polynomial import Polynomial, Point
import unittest

class TestInitializer(unittest.TestCase):

    def test_point_init(self):
        poly = Polynomial(Point(1, 2), Point(2, 4), Point(3, 8), Point(0, -5))
        self.assertEqual(poly.degree, 3)


if __name__ == '__main__':
    unittest.main()
