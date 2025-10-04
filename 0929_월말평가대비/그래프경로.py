t = int(input())
for test_case in range(1,t+1):
    ans = 0

    def dfs(start_v):
        global ans
        if start_v == G:
            ans = 1
            return
        if ans == 1:
            return
        for i in child[start_v]:
            dfs(i)


    V , E = map(int,input().split())
    child = [[] for _ in range(V+1)]
    for _ in range(E):
        a,b = map(int,input().split())
        child[a].append(b)
    
    S, G = map(int,input().split())
    dfs(S)
    print(f"#{test_case} {ans}")