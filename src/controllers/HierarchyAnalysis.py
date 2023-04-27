import functools

from src.controllers.SimpleRanking import SimpleRanking


class HierarchyAnalysis(object):
    array: [[int]]

    def __init__(self, arr: [[int]]):
        self.judgments = arr

    def calc(self):
        p = []
        p_avg = []
        vector_kov = []
        for i in self.judgments:
            el = functools.reduce(lambda a, b: a * b, i)
            p.append(el)
            p_avg.append(el ** (1 / len(self.judgments)))
        print(f"П = {list(map(lambda a: round(a, 3), p))}")
        print(f"П^1/{len(self.judgments)} = {list(map(lambda a: round(a, 3), p_avg))}")
        p_sum = sum(p_avg)
        print(f"sum(П^1/{len(self.judgments)}) = {round(p_sum, 3)}")
        vector_kov = list(map(lambda a: a / p_sum, p_avg))
        print(f"Вектор КОВ ={list(map(lambda a: round(a, 3), vector_kov))} \nsum = {round(sum(vector_kov), 1)} ")
        return vector_kov


criteria = [
    [1, 1 / 4, 3, 1 / 3, 1 / 5],
    [4, 1, 5, 3, 1 / 3],
    [1 / 3, 1 / 5, 1, 1 / 5, 1 / 7],
    [3, 1 / 3, 5, 1, 1 / 4],
    [5, 3, 7, 4, 1]
]
variants_k1 = [
    [1, 4, 3, 6],
    [1 / 4, 1, 1 / 2, 3],
    [1 / 3, 2, 1, 4],
    [1 / 6, 1 / 3, 1 / 4, 1]
]
variants_k2 = [
    [1, 3, 1 / 3, 4],
    [1 / 3, 1, 1 / 5, 2],
    [2, 3, 1, 5],
    [1 / 4, 1 / 2, 1 / 5, 1]
]
variants_k3 = [
    [1, 5, 3, 4],
    [1 / 5, 1, 1 / 4, 1 / 3],
    [1 / 3, 4, 1, 2],
    [1 / 4, 3, 1 / 2, 1]
]
variants_k4 = [
    [1, 3, 2, 1 / 2],
    [1 / 3, 1, 1 / 2, 1 / 4],
    [1 / 2, 2, 1, 1 / 2],
    [2, 4, 2, 1]
]
variants_k5 = [
    [1, 1 / 3, 2, 1 / 4],
    [3, 1, 4, 1 / 2],
    [1 / 2, 1 / 4, 1, 1 / 5],
    [4, 2, 5, 1]
]
print(f"")
z = HierarchyAnalysis(criteria).calc()
print(200 * "-")
b = [HierarchyAnalysis(variants_k1).calc()]
print(200 * "-")
b.append(HierarchyAnalysis(variants_k2).calc())
print(200 * "-")
b.append(HierarchyAnalysis(variants_k3).calc())
print(200 * "-")
b.append(HierarchyAnalysis(variants_k4).calc())
print(200 * "-")
b.append(HierarchyAnalysis(variants_k5).calc())

w = []
for i in range(len(z)):
    w_sum = 0
    for j in b[i]:
        w_sum += j * z[i]
    w.append(w_sum)

print(list(map(lambda a: round(a, 3), w)))
print(sum(w))
