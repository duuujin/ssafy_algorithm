# 김싸피에게는 생성 가능한 M개의 시냅스 후보 목록이 있으며, 각 후보는 어떤 뉴런과 어떤
# 뉴런을 연결하며, 이때 얼마의 에너지 비용이 드는지에 대한 정보를 담고 있습니다.
# 김싸피를 도와, 모든 뉴런을 하나의 네트워크로 연결하는 데 필요한 최소 총 에너지 비용을
# 계산하세요. 만약 모든 뉴런을 연결하는 것이 불가능하다면 -1을 출력합니다.

# [입력]
# 첫 줄에 테스트케이스 수 T, 다음 줄부터 각 케이스 별로 첫 줄에 뉴런의 수 N 과 시냅스 후보의
# 수 M이 주어집니다. 이어서 M개의 줄에 걸쳐 각 시냅스 연결에 대한 정보 Xi
# , Yi
# , costi 가
# 주어집니다.
# ( 1 <= T <= 10, 1 <= N, M <= 104
# , 1 <= Xi
# , Yi <= N, 1 <= costi <= 105
# , Xi != Yi
# )
# [출력]
# - 모든 뉴런을 하나의 네트워크로 연결하는 데 필요한 최소 총 에너지 비용을 출력합니다.
# - #과 1번부터인 테스트케이스 번호, 빈칸에 이어 최소 비용을 구분해 출력합니다.
class Disjointset:
    def __init__(self,v):
        self.p = list(range(v + 1))
        self.rank = [0] * (v + 1)
    
    def find_set(self,x):
        if x != self.p[x]:
            self.p[x] = self.find_set(self.p[x])
        return self.p[x]

    def union(self, x, y):
        px = self.find_set(x)
        py = self.find_set(y)

        if px != py :
            if self.rank[px] < self.rank[py]:
                self.p[px] = py
            elif self.rank[px] > self.rank[py]:
                self.p[py] = px
            else:
                self.p[py] = px
                self.rank[px] += 1
            return True
        return False

def mst_kruskal(v, edges):
    ds = Disjointset(v)
    edges.sort(key= lambda x: x[2])
    total_weight = 0
    edge_count = 0

    for edge in edges:
        n1, n2, w = edge
        if ds.union(n1,n2):
            total_weight += w
            edge_count += 1
            if edge_count == (v - 1):
                break
    
    if edge_count < v - 1:
        return -1
    return total_weight


T = int(input())
for test_case in range(1,T+1):
    N,M = map(int,input().split())
    edges = []
    for _ in range(M):
        n1, n2, w = map(int,input().split())
        edges.append((n1, n2, w))
    
    result = mst_kruskal(N,edges)
    print(f'#{test_case} {result}')