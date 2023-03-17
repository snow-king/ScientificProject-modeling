import math

import numpy as np
from numpy.random import default_rng

from src.controllers.NormalDistribution import NormalDistribution
from src.controllers.StaticInfoHandler import StaticInfoHandler


class LogNormalDistribution(object):
    mathematicalExpect: float
    dispersion: float
    sampleY: list[float]
    sampleX: list[float]
    alpha: float
    beta: float

    def __init__(self, mathematical_expect=5, dispersion=1):
        self.mathematicalExpect = mathematical_expect
        self.dispersion = dispersion

    def calc_alpha(self):
        self.alpha = np.log(self.mathematicalExpect) - (self.beta ** 2) / 2
        print(f'alpha = {self.alpha}')
        return self.alpha

    def calc_beta(self):
        self.beta = np.log(1 + self.dispersion / (self.mathematicalExpect ** 2)) ** 0.5
        print(f'beta = {self.beta}')
        return self.beta

    def generate_sample_y(self):
        normal = NormalDistribution(self.alpha, self.beta)
        self.sampleY = normal.generate()
        print(self.sampleY)

    def generate_sample_x(self):
        self.sampleX = [math.exp(i) for i in self.sampleY]
        print(self.sampleX)
        return self.sampleX

    def check_sample(self):
        checker = StaticInfoHandler()
        checker.set_sample(self.sampleX)
        checker.run()

    def run(self):
        self.calc_beta()
        self.calc_alpha()
        self.generate_sample_y()
        self.generate_sample_x()
        self.check_sample()


hz = LogNormalDistribution()
hz.run()
