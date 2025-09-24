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

disjoint_set = DisjointSet([1, 2, 3, 4, 5, 6])

for i in range(1, len(disjoint_set.p)):
    disjoint_set.make_set(i)

# 간선 추가
edges = [(1, 2), (2, 3), (4, 5), (5, 6), (3, 4)]

# 간선을 통해 유니온 연산 수행
for i, (u, v) in enumerate(edges):
    disjoint_set.union(u, v)

