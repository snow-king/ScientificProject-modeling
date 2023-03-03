import numpy as np

from numpy.random import default_rng


class StaticInfoHandler(object):
    mathematicalExpect: float
    sample: list[float]
    dispersion = 0
    standardDeviation: float
    RMS: float
    interval: [float]

    def __init__(self):
        self.sample = [i * 3 for i in default_rng().random(1000)]

    def mathematical_expectation(self) -> float:
        expect = 0
        for i in self.sample:
            expect += i / len(self.sample)
        self.mathematicalExpect = expect
        return self.mathematicalExpect

    def dispersion_calc(self):
        mean = (sum(self.sample) / len(self.sample))
        expect = sum([d**2 for d in [(v - mean) for v in self.sample]])/ (len(self.sample) - 1)
        self.dispersion = expect
        return self.dispersion

    def rms_calc(self):
        self.RMS = self.dispersion ** 0.5
        return self.RMS

    def interval_calc(self):
        z = 1.96
        sigma = 1.96 * self.RMS / (len(self.sample) ** 0.5)
        y1 = self.mathematicalExpect - sigma
        y2 = self.mathematicalExpect + sigma
        print(f"y1={y1} y2={y2}")
        if y1 <= self.mathematicalExpect <= y2:
            print("математическое ожидание попало в доверительный интервал")
        else:
            print("математическое ожидание не попало в доверительный интервал")

    def show_results(self):
        print(f"Выборка: {self.sample}")
        print(f"Мат. Ожидание: {self.mathematicalExpect}")
        print(f"Дисперсия {self.dispersion}")
        print(f"Cреднеквадратическое отклонение: {self.dispersion ** 0.5}")
        self.interval_calc()

    def set_sample(self, list_rand):
        self.sample = list_rand

    def run(self):
        self.mathematical_expectation()
        self.dispersion_calc()
        self.rms_calc()
        self.show_results()
