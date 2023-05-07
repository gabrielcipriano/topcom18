from sys import stdin
from math import sqrt
from itertools import combinations


def calculate(n):
    if n <= 0: return 1
    for x in range(1, n*3):
        arr = list(range(x))
        totalCombinations = len(list(combinations(arr, 2)))
        if totalCombinations == n:
            return x
        if totalCombinations > n:
            return x-1
    

ntests = 0
for i, line in enumerate(stdin):
    if i == 0:
        ntests = int(line)
        continue
    print(calculate(int(line)))