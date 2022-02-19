import numpy as np
import re

# maybe clean up x^1 into just x and don't display 0 terms
class Polynomial:
    def __init__(self, points, coeffs=None):
        assert(type(points == list))
        # points list should look like [[x1, y1], [x2, y2], ... ]
        # or [Point1, Point2, Point3, ...]
        if points:
            self.points = points
            self.degree = len(points) - 1
            constants = np.array([p[1] for p in points])
            #constants = [point.x for point in list]
            x_vals = self.get_x_coeffs()
            self.coeffs = np.linalg.solve(x_vals, constants)
        elif coeffs:
            self.coeffs = coeffs
            self.degree = len(coeffs) - 1
        else:
            assert("Please enter either a list of points or a list of coefficients")


    def __str__(self):
        return clean_str(str_helper(self.coeffs, self.degree))

    def get_integral(self):
        coeffs = integral_helper(self.degree, self.coeffs)
        return Polynomial(None, coeffs=coeffs)

    def get_x_coeffs(self):
        #take in a list of x values, return a matrix of coefficients
        coeffs = []

        for x in self.points:
            eq = []
            for num in range(self.degree + 1):
                eq.insert(0, x[0] ** num)
                # eq.insert(0, x.x ** num)
            coeffs.append(eq)
        return np.array(coeffs)

    
def integral_helper(degree, coeffs):
    if degree == 0:
        return []
    return [coeffs[0] * degree] + integral_helper(degree - 1, coeffs[1:])

def str_helper(sols, degree):
    a = sols[0]
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
            return f'x^{degree} + ' + str_helper(sols[1:], degree - 1)
        elif a == -1:
            return f'-x^{degree} + ' + str_helper(sols[1:], degree - 1)
        return f'{a}x^{degree} + ' + str_helper(sols[1:], degree - 1)

def clean_str(s):
    return s.replace("+ -", '- ')

poly = Polynomial([[1, 2], [2, 4], [3, 8], [0, 5]])
# quadratic = Polynomial(Point(1, 2), Point(2, 4), Point(3, 8))
print(poly)
print(poly.get_integral())





