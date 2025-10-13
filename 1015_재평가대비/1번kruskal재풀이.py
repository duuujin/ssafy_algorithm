class Disjointset:
    def __init__(self,v):
        self.p = list(range(v + 1))
        self.rank = [0] * (v + 1)
    
    def find_set(self,x):
        if x != self.p[x]:
            self.p[x] = self.find_set(self.p[x])
        return self.p[x]

    def union(self,x,y):
        px = self.find_set(x)
        py = self.find_set(y)

        if px != py:
            if self.rank[px] < self.rank[py]:
                self.p[px] = py
            elif self.rank[px] > self.rank[py]:
                self.p[py] = px
            else:
                self.p[py] = px
                self.rank[px] += 1
            return True
        return False

def kruskal(v, edges):
    ds = Disjointset(v)
    edges.sort(key=lambda x : x[2])
    total_weight = 0
    edge_count = 0

    for edge in edges:
        n1, n2, w = edge
        if ds.union(n1,n2):
            total_weight += w
            edge_count += 1
            if edge_count == ( v - 1):
                break
    
    if edge_count < ( v - 1):
        return -1
    return total_weight

T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    edges = []
    for _ in range(M):
        n1, n2, w = map(int,input().split())
        edges.append((n1,n2,w))
    
    result = kruskal(N, edges)
    print(f'#{test_case} {result}')