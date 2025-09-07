from itertools import combinations, permutations, product, combinations_with_replacement
n = 10
k1 = 8
k2 = 10
for idx in combinations(range(1,n+1), 2):
    print(list(idx))