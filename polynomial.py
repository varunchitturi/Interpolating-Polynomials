import numpy as np

# need to make it dispay ints without the .0 (can probably
# do this by checking sol[0] % 1 or smth) and round floats
# to 2-3 digits. also + followed by minus should become -1
# (this part can be done with a clean string method?)
class Polynomial:
    
    coeffecients = []

    def __init__(self, points):
        assert(type(points == list))
        # points list should look like [[x1, y1], [x2, y2], ... ]
        # or [Point1, Point2, Point3, ...]
        self.points = points
        self.degree = len(points) - 1
        constants = np.array([p[1] for p in points])
        #constants = [point.x for point in list]

        coeffs = self.get_coeffs()

        self.sol = np.linalg.solve(coeffs, constants)

    def __str__(self):
        return str_helper(self.sol, self.degree)

    def get_coeffs(self):
        #take in a list of x values, return a matrix of coefficients
        coeffs = []

        for x in self.points:
            eq = []
            for num in range(self.degree + 1):
                eq.insert(0, x[0] ** num)
                # eq.insert(0, x.x ** num)
            coeffs.append(eq)
        return np.array(coeffs)

def str_helper(sols, degree):
    if degree == 0:
        return str(sols[0])
    return f'{sols[0]} x ^ {degree} + ' + str_helper(sols[1:], degree - 1)

quadratic = Polynomial([[1, 2], [2, 4], [3, 8]])
# quadratic = Polynomial(Point(1, 2), Point(2, 4), Point(3, 8))
print(quadratic)





