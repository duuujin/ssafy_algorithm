def find(x):
    if x != p_list[x]:
        p_list[x] = find(p_list[x])
    return p_list[x]

def union(x,y):
    px = find(x)
    py = find(y)
    if px < py:
        p_list[py] = px
    else:
        p_list[px] = py

T = int(input())
for test_case in range(1,T+1):
    n, m = map(int,input().split())
    ans = []
    p_list = list(range(n+1))
    for _ in range(m):
        e, a, b = map(int,input().split())
        if e == 0:
            union(a,b)
        else:
            if find(a) == find(b):
                ans.append('1')
            else:
                ans.append('0')
    print(f'#{test_case} {"".join(ans)}')