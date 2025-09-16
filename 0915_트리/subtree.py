# dfs 카운트
def dfs(node):
    if node == 0:
        return 0
    return 1 + dfs(child1[node]) + dfs(child2[node])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    child1 = [0]*(E+2)
    child2 = [0]*(E+2)

    for i in range(E):
        p, c = arr[2*i], arr[2*i+1]
        if child1[p] == 0:
            child1[p] = c
        else:
            child2[p] = c

    ans = dfs(N)
    print(f"#{tc} {ans}")

# -------------------------------------
# 인접리스트 방식
def dfs(node):
    cnt = 1
    for nxt in child[node]:
        cnt += dfs(nxt)
    return cnt

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    child = [[] for _ in range(E+2)]

    for i in range(E):
        parent = arr[2*i]
        c = arr[2*i+1]
        child[parent].append(c)

    ans = dfs(N)
    print(f"#{tc} {ans}")
