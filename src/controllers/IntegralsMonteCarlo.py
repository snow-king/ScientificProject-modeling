import math
import typing

import numpy as np
import numpy.random


class IntegralCalc(object):
    lambed: float
    a: float
    b: float
    R: float
    scopeR: float
    analyticalFunc: typing.Callable
    integralFunc: typing.Callable
    iterations: int

    def __init__(self, analytic: typing.Callable, integral: typing.Callable, lambed=1.5, a=1, b=4, n=10000):
        self.lambed = lambed
        self.a = a
        self.b = b
        self.analyticalFunc = analytic
        self.integralFunc = integral
        self.iterations = n

    def calc_analytical_value(self):
        print()
        print(f"Аналитическое решение (формула Ньютона-Лейбница):"
              f"{self.analyticalFunc(self.b, self.lambed) - self.analyticalFunc(self.a, self.lambed)}")

    def monte_carlo_calc(self):
        self.R = 0
        self.scopeR = 0
        rng = np.random.default_rng()
        for i in range(self.iterations):
            ri = numpy.random.random()
            xi = - math.log(ri) / self.lambed
            xi2 = (self.b - self.a) * ri + self.a
            if self.a <= xi <= self.b:
                self.R += xi ** 2 / self.lambed
            self.scopeR += self.integralFunc(self.a, self.b, self.lambed, xi2)
        # print(self.R / self.iterations)
        print(f'Решение с помощью метода  Монте-Карло : {self.scopeR / self.iterations}')

    def run(self):
        self.calc_analytical_value()
        self.monte_carlo_calc()


def f1(x, lambed):
    return - math.pow(math.e, -(lambed * x)) * (
            (x * x / lambed) + (2 * x) / (lambed * lambed) + 2 / math.pow(lambed, 3.0))


def f2(x, lambed):
    return -(math.e ** (-lambed * x) / (lambed ** 2 + 1)) * (lambed * math.sin(x) + math.cos(x))


def f3(x, lambed):
    return (math.pow(math.e, -lambed * x) / (lambed * lambed + 1)) * (math.sin(x) - lambed * math.cos(x))


def integral1(a, b, lambed, x):
    return (b - a) * (x ** 2) * math.pow(math.e, -lambed * x)


def integral2(a, b, lambed, x):
    return (b - a) * math.sin(x) * math.pow(math.e, -lambed * x)


def integral3(a, b, lambed, x):
    return (b - a) * math.cos(x) * math.pow(math.e, -lambed * x)


answer1 = IntegralCalc(f1, integral1)
answer1.run()
answer2 = IntegralCalc(f2, integral2)
answer2.run()
answer2 = IntegralCalc(f3, integral3)
answer2.run()
