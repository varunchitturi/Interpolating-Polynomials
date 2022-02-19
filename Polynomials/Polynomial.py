from .Point import Point
import numpy as np


# TODO: maybe make it so 0 terms aren't displayed
class Polynomial:
    """
    A type to hold polynomial equations
    """

    def __init__(self, *points: Point, coeffs=None):
        """

        :param points: The points that the polynomial intersects
        :param coeffs: A list of coefficients of the polynomial
        """

        if points:
            self.points = points
            self.degree = len(points) - 1
            constants = [point.y for point in points]
            x_vals = self.get_x_coeffs()
            self.coeffs = np.linalg.solve(x_vals, constants)
        elif coeffs:
            self.coeffs = coeffs
            self.degree = len(coeffs) - 1
        else:
            assert "Please enter either a list of points or a list of coefficients"

    def __str__(self):
        return Polynomial._clean_str(Polynomial._str_helper(self.coeffs, self.degree))

    def get_derivative(self):
        """

        :return: Returns the derivative of a polynomial
        """
        coeffs = Polynomial._derivative_helper(self.degree, self.coeffs)
        return Polynomial(coeffs=coeffs)

    def get_integral(self):
        """

        :return: Returns the integral of a polynomial
        """
        coeffs = Polynomial._integral_helper(self.degree, self.coeffs)
        return Polynomial(coeffs=coeffs)

    def get_x_coeffs(self):
        """

        :return: A coefficient matrix of a polynomial
        """
        coeffs = []

        for point in self.points:
            eq = []
            for degree in range(self.degree + 1):
                eq.insert(0, point.x ** degree)
            coeffs.append(eq)
        return np.array(coeffs)

    @staticmethod
    def _clean_str(string):
        return string.replace("+ -", '- ').replace('x^1 ', 'x ')

    @staticmethod
    def _derivative_helper(degree, coeffs):
        if degree == 0:
            return []
        return [coeffs[0] * degree] + Polynomial._derivative_helper(degree - 1, coeffs[1:])

    @staticmethod
    def _integral_helper(degree, coeffs):
        if degree == 0:
            return [coeffs[0]] + ['C']
        return [coeffs[0] / (degree + 1)] + Polynomial._derivative_helper(degree - 1, coeffs[1:])

    @staticmethod
    def _str_helper(sols, degree):
        a = sols[0]

        if type(a) != str:
            a = round(a * 1000)/1000.0
            if a % 1.0 in [0, 0.0]:
                a = int(a)

        if degree == 0:
            if a == 1:
                return ''
            elif a == -1:
                return '-'
            return str(a) if a != 1 else ''
        else:
            if a == 1:
                return f'x^{degree} + ' + Polynomial._str_helper(sols[1:], degree - 1)
            elif a == -1:
                return f'-x^{degree} + ' + Polynomial._str_helper(sols[1:], degree - 1)
            return f'{a}x^{degree} + ' + Polynomial._str_helper(sols[1:], degree - 1)



