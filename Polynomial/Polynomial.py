from zipfile import LargeZipFile
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

    def __eq__(self, obj):
        ob1Coeffs = self.coeffs
        ob2Coeffs = obj.coeffs
        if ob1Coeffs[-1] == ob2Coeffs[-1] and ob1Coeffs[-1] == 'C' and ob2Coeffs[-1] == 'C':
            ob1Coeffs.pop()
            ob2Coeffs.pop()
        elif obj.coeffs[-1] != self.coeffs[-1]:
            return False

        return [round(float(x), 12) for x in list(ob1Coeffs)] == [round(float(x), 12) for x in list(ob2Coeffs)] and self.degree == obj.degree

    def plot(self):
        """

        Plots a graph of the polynomial
        """
        # TODO: DO PLOT

    def polynomial_sum(self, poly_2):
        """
        
        Returns a sum of two polynomials
        """
        bigger_polynomial = max(self, poly_2, key=lambda x:len(x.coeffs))
        smaller_polynomial = min(self, poly_2, key=lambda x:len(x.coeffs))

        result = []
        for i in range(1, len(smaller_polynomial.coeffs) + 1):
            result.insert(0, bigger_polynomial.coeffs[-i] + smaller_polynomial.coeffs[-i])
        for i in range(len(smaller_polynomial.coeffs) + 1, len(bigger_polynomial.coeffs) + 1):
            result.insert(0, bigger_polynomial.coeffs[-i])

        return Polynomial(coeffs=result)
    
    def get_derivative(self):
        """

        :return: Returns the derivative of a polynomial
        """
        coeffs = Polynomial._derivative_helper(self.degree, self.coeffs)
        return Polynomial(coeffs=coeffs)

    def get_integral(self, C='C'):
        """

        :return: Returns the integral of a polynomial
        """
        coeffs = Polynomial._integral_helper(self.degree, self.coeffs, C)
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

    def evaluate(self, x):
        """

        :return: Returns the value of a polynomial at a given point
        """
        x_vector = []
        for degree in range(self.degree + 1):
            x_vector.insert(0, x ** degree)
        x_vector = np.array(x_vector)
        return np.matmul(self.coeffs, x_vector)

    def find_root(self, init_guess):
        """

        :return: Returns a root of a polynomial given an initial guess
        """
        y = self.evaluate(init_guess)
        if round(y * 1000) / 1000 == 0:
            return init_guess
        try:
            y_prime = self.get_derivative().evaluate(init_guess)
            return self.find_root(init_guess - y / y_prime)
        except RecursionError as e:
            return None

    def find_roots_range(self, min, max, width=1):
        """

        :return: Returns a list of all roots of a polynomial over a given range
        """
        solutions = []
        while min <= max:
            if self.find_root(min):
                sol = round(1000 * self.find_root(min)) / 1000
                if sol not in solutions:
                    solutions.append(sol)
            min += width
        return solutions

    @staticmethod
    def _clean_str(string):
        return string.replace("+ -", '- ').replace('x^1 ', 'x ')

    @staticmethod
    def _derivative_helper(degree, coeffs):
        if degree == 0:
            return []
        return [coeffs[0] * degree] + Polynomial._derivative_helper(degree - 1, coeffs[1:])

    @staticmethod
    def _integral_helper(degree, coeffs, C):
        if degree == 0:
            return [coeffs[0], C]
        return [coeffs[0] / (degree + 1)] + Polynomial._integral_helper(degree - 1, coeffs[1:], C)

    @staticmethod
    def _str_helper(sols, degree):
        a = sols[0]

        if type(a) != str:
            a = round(a * 1000) / 1000.0
            if a % 1.0 in [0, 0.0]:
                a = int(a)

        if degree == 0:
            return str(a)
        else:
            if a == 1:
                return f'x^{degree} + ' + Polynomial._str_helper(sols[1:], degree - 1)
            elif a == -1:
                return f'-x^{degree} + ' + Polynomial._str_helper(sols[1:], degree - 1)
            return f'{a}x^{degree} + ' + Polynomial._str_helper(sols[1:], degree - 1)
