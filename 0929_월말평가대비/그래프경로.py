def dfs(s):
    global ans
    if s == G : 
        ans += 1
        return
    if ans == 1:
        return
    for i in child[s]:
        dfs(i)

T = int(input())
for test_case in range(1,T+1):
    ans = 0
    V , E = map(int,input().split())
    child = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int,input().split())
        child[a].append(b)
    S,G = map(int,input().split())
    dfs(S)
    print(f'#{test_case} {ans}')