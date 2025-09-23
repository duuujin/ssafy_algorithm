def make_set(n):
    parent = [i for i in range(n + 1)]
    rank = [0] * (n + 1)
    return parent, rank

def find_set(x):
    if parent[x] == x:
        return x
    return find_set(parent[x])

def union_by_rank(x, y):
    pass


parent, rank = make_set(6)
print(f"초기 상태:")
print(f"parent: {parent}")
print(f"rank:   {rank}")
print()

print("union(1, 2):")
union_by_rank(1, 2)  # rank(1)이 1로 증가
print(f"parent: {parent}")
print(f"rank:   {rank}")
print()

print("union(3, 4):")
union_by_rank(3, 4)  # rank(3)이 1로 증가
print(f"parent: {parent}")
print(f"rank:   {rank}")
print()

print("union(1, 3):")
union_by_rank(1, 3)  # 랭크가 같으므로 rank(1)이 2로 증가
print(f"parent: {parent}")
print(f"rank:   {rank}")
print()

print("union(1, 6):")
union_by_rank(1, 6)  # rank(1)변화 없음.
print(f"parent: {parent}")
print(f"rank:   {rank}")


