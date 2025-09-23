def make_set(n):
    return [i for i in range(n + 1)]

def find_set_pc(x):
    pass

def union(x, y):
    root_x = find_set_pc(x)
    root_y = find_set_pc(y)
    if root_x != root_y:
        parent[root_y] = root_x


parent = make_set(6)

union(5, 6)
union(4, 5)
union(3, 4)
union(2, 3)
union(1, 2)
print(f"긴 트리 상태: {parent}")

find_set_pc(6)
print(f"경로 압축 후: {parent}")