from Polynomial import Polynomial, Point


def main():
    poly = Polynomial(Point(1, 2), Point(2, 4), Point(3, 8), Point(0, -5))
    print('calculated polynomial:', poly)
    print('derivative:', poly.get_derivative())
    print('integral', poly.get_integral())


if __name__ == "__main__":
    main()



