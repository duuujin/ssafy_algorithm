import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a_root = find(parent, a)
    b_root = find(parent, b)
    if a_root == b_root:
        return False
    parent[b_root] = a_root
    return True

def kruskal(N, edges):
    edges.sort(key=lambda x: x[2])
    parent = {i: i for i in range(1, N+1)}
    mst_cost = 0
    mst_edges = []
    
    for u, v, w in edges:
        if union(parent, u, v):
            mst_cost += w
            mst_edges.append((u, v, w))
    
    if len(mst_edges) != N - 1:
        return -1
    total_cost = sum(w for _, _, w in edges)
    return total_cost - mst_cost

# 입력
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

result = kruskal(N, edges)
print(result)
