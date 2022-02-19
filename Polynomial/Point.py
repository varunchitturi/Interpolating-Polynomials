class Point:
    """
    A type to hold a point in a cartesian coordinate plane
    """
    def __init__(self, x, y):
        """

        :param x: X value of the point
        :param y: Y value of the point
        """
        print(type(x), type(y))
        assert (type(x) == int or type(x) == float) and (type(y) == int or type(y) == float), \
            "X and Y values must be numerical"

        self.x = x
        self.y = y

    def __eq__(self, obj):
        return self.x == obj.x and self.y == obj.y