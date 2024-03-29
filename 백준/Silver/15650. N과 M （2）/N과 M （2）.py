from itertools import combinations

N, M = map(int, input().split())

comb = list(combinations(range(1, N + 1), M))

for c in comb:
    print(*c)