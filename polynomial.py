from typing import List, Any
from coordinate import Coordinate

class Polynomial:

    coefficients: List[int] = []

    def __init__(self, *points):
        """

        :param points: List of points that the polynomial goes through
        :type points: Coordinate
        """
        print()
