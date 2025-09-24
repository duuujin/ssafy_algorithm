class DisjointSet:
    # 생성자 메서드
    def __init__(self, v):
        # 각 정점의 대표자를 가리키는 리스트
        # 각 정점의 랭크를 저장하기 위한 리스트
        self.p = [0] * (len(v) + 1)
        self.rank = [0] * (len(v) + 1)

    # 집합을 만드는 메서드
    # 각 노드가 자기 자신을 부모로 가지도록 초기화
    def make_set(self, x):
        self.p[x] = x   # 스스로를 대표자로 설정
        self.rank[x] = 0    # 초기 랭크는 0

    # 대표자를 반환하는 메서드
    def find_set(self, x):
        if x != self.p[x]: # 들어온 x가 대표자가 아닌 경우, 다시 부모를 타고 올라감.
            # 경로 압축 -> 재귀를 빠져난올 때, 각 노드들의 대표자를 갱신
            self.p[x] = self.find_set(self.p[x])
        return self.p[x]

    # 집합을 합병하는 메서드
    def union(self, x, y):
        # 대장전을 해야한다. 그래서 x,y의 대표자를 가져온다
        px = self.find_set(x)
        py = self.find_set(y)

        # 같은 집합이면 합병하지 않는다.
        if px != py:
            if self.rank[px] < self.rank[py]:
                self.rank[px] = py
            elif self.rank[px] > self.rank[py]:
                self.p[py] = px
            else:   # 두 대표자의 랭크가 같을 경우
                self.p[py] = px
                self.rank[px] += 1

def mst_kruskal(vertices, edges):
    # disjoint set 만들고, make_set으로 초기화
    mst = []
    ds = DisjointSet()
    for i in range(len(vertices) + 1):
        ds.make_set(i)

    # 1. 가중치를 기준으로 오름차순 정렬
    edges.sort(key=lambda x: [x])

    # 2. 정렬된 가중치를 하나씩 순회하면서 합병한다. (싸이클을 형성하지 않는 조건으로)
    for edge in edges:
        s, e, w = edge  # 시작정점, 도착정점, 가중치

        # 싸이클이 형성되는지를 확인 - > 대표자가 같은지 확인
        if ds.find_set(s) != ds.find_set(e):    # 시작정점의 대표자와 도착정점의 대표자가 다르면, 싸이클 형성 X -> 최소신장트리에 목록에 추가
            ds.union(s,e)
            mst.append(edge)


# [시작정점, 도착정점, 가중치]
edges = [[1, 2, 1], [2, 3, 3], [1, 3, 2]]
vertices = [1, 2, 3]  # 정점 집합


result = mst_kruskal(vertices, edges)  # [[1, 2, 1], [1, 3, 2]]
print(result)


# 교재 간선 정보
edges = [
    (0, 1, 32),
    (0, 2, 31),
    (0, 5, 60),
    (0, 6, 51),
    (1, 2, 21),
    (2, 4, 46),
    (2, 6, 25),
    (3, 4, 34),
    (3, 5, 18),
    (4, 5, 40),
    (4, 6, 51),
]
vertices = list(range(7))  # 정점 집합

result = mst_kruskal(vertices, edges)
print(result) # [(3, 5, 18), (1, 2, 21), (2, 6, 25), (0, 2, 31), (3, 4, 34), (2, 4, 46)]