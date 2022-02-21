from Polynomial import Polynomial, Point


def main():

    print("Question 1:")
    poly = Polynomial(Point(1,29), Point(-1,-35), Point(2,31), Point(-3,-19))
    print('calculated polynomial:', poly, '\n')

    print('Question 2:')
    poly = Polynomial(Point(-1, 0.5), Point(0,1), Point(1,2), Point(2,4), Point(3,8))
    print('calculated polynomial:', poly, '\n')

if __name__ == "__main__":
    main()



