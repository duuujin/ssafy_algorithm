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

def kruskal(vertices, edges):
    global total_cost, min_cost
    edges.sort(key=lambda x: x[2])
    parent = {v: v for v in vertices}
    mst_cost = 0
    mst_edges = []
    
    for u, v, w in edges:
        if union(parent, u, v):
            mst_cost += w
            mst_edges.append((u, v, w))
    
    if len(mst_edges) != len(vertices) - 1:
        return -1
    return total_cost - mst_cost

N,M = map(int,input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
vertices = list({v for edge in edges for v in edge[:2]})

total_cost = sum(w for _,_, w in edges)
min_cost = 0
result = kruskal(vertices, edges)

print(result)
