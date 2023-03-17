from numpy.random import default_rng


class NormalDistribution(object):
    mathematicalExpect: float
    dispersion: float
    sample: list[float]

    def __init__(self, mathematical_expect=5, dispersion=1):
        self.mathematicalExpect = mathematical_expect
        self.dispersion = dispersion

    def generate(self):
        self.sample = [self.mathematicalExpect + self.dispersion * sum([i for i in default_rng().random(1000)]) - 6 for
                       j in range(1000)]
        print(self.sample)


normal = NormalDistribution()
normal.generate()
