<<<<<<< HEAD
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
=======
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
>>>>>>> 485c0c243f167de6e4c6f277a98ebbab412eba7a
