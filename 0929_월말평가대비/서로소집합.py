def find(x):
    if x != p_list[x]:
        p_list[x] = find(p_list[x])
    return p_list[x]

def union(x,y):
    px = find(x)
    py = find(y)
    if px < py:
        p_list[px] = py
    else:
        p_list[py] = px

T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    p_list = list(range(N+1))
    ans = []
    for _ in range(M):
        e, a, b = map(int,input().split())
        if e == 0:
            union(a,b)
        else:
            if find(a) == find(b):
                ans.append("1")
            else:
                ans.append("0")
    
    print(f'#{test_case} {"".join(ans)}')