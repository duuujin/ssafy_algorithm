def make_set(n):
    pass

def find_set(x):
    pass

def union(x, y):
    pass

parent = make_set(6)
print(f"초기 상태: {parent}")

union(5, 6)
union(4, 5)
union(3, 4)
union(2, 3)
union(1, 2)

print(f"연산 후 상태: {parent}")