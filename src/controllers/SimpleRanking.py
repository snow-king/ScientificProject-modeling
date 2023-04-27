class SimpleRanking(object):
    judgments: [[int]]
    full_sum: int
    kov: [float]
    L: int
    Q: int
    s_stat: float
    concard: float

    def __init__(self, arr: [[int]]):
        self.judgments = arr
        self.q = len(arr)
        self.L = len(arr[0])

    def sum(self):
        self.full_sum = 0
        for i in self.judgments:
            self.full_sum += sum(i)
        print(f"сумма оценок: {self.full_sum}")

    def calc_kow(self):
        self.sum()
        self.kov = [sum(i) / self.full_sum for i in self.judgments]
        print(f"коэффициентов относительной важности: {self.kov}")
        return self.kov

    def s_statistics(self):
        self.s_stat = 0
        for i in self.judgments:
            self.s_stat += (sum(i) - self.L * (self.q + 1) / 2) ** 2
        print(f"S-статистика : {self.s_stat}")

    def concordance_factor(self):
        self.concard = (12 * self.s_stat) / (self.L ** 2 * (self.q ** 3 - self.q))
        print(f"Коэффициент конкордации {self.concard}")


# rank = SimpleRanking([
#     [3, 4, 4, 3, 4],
#     [2, 3, 3, 4, 2],
#     [4, 1, 2, 2, 3],
#     [1, 2, 1, 1, 1]
# ])
# rank.calc_kow()
# rank.s_statistics()
# rank.concordance_factor()
