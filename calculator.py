import math





class Basic:

    def __init__(self):
        pass

    def a(self, x, y):
        return x + y

    def s(self, x, y):
        return x - y

    def m(self, x, y):
        return x * y

    def d(self, x, y):
        return x / y


# add lots more methods to this calculator class.


class Intermediate:

    def square(self, x):
        return x ** 2
        # print("Square = ", result)

    def squareroot(self, x):
        return math.sqrt(x)
        # print("Squareroot = ", result)

    def exponential(self, x, y):
        return x ** y
        # print("Exponential = ", result)

    def sine(self, x):
        return math.sin(x)
        # print("sin = ", result)

    def cosine(self, x):
        return math.cos(x)
        # print("cos = ", result)

    def tang(self, x):
        return math.tan(x)
        # print("tan = ", result)

    def asine(self, x):
        return math.asin(x)
        # print("inverse sin = ", result)

    def acosine(self, x):
        return math.acos(x)
        # print("inverse cos = ", result)

    def atang(self, x):
        return math.atan(x)
        # print("inverse tan = ", result)


# answer = intermediate()

# print(a.self(4, 1))
