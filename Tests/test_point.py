from Polynomial import Point
import unittest


class TestInitializer(unittest.TestCase):
    def test_int_init(self):
        p1 = Point(1, 2)
        self.assertEqual(p1.x, 1)
        self.assertEqual(p1.y, 2)

    def test_float_init(self):
        p1 = Point(1.1, 2.2)
        self.assertEqual(p1.x, 1.1)
        self.assertEqual(p1.y, 2.2)

    def test_error_str_init(self):
        with self.assertRaises(Exception):
            p1 = Point("1.1", "2.2")


class TestMethods(unittest.TestCase):
    def test_equals_true(self):
        p1 = Point(1.1, 2.2)
        p2 = Point(1.1, 2.2)
        self.assertEqual(p1, p2)

    def test_equals_false(self):
        p1 = Point(1.1, 2.2)
        p2 = Point(1, 2)
        self.assertNotEqual(p1, p2)


if __name__ == '__main__':
    unittest.main()
