def find(x):
    if x != p_list[x]:
        p_list[x] = find(p_list[x])
    return p_list[x]

def union(x,y):
    px = find(x)
    py = find(y)
    if px != py:
        p_list[py] = px

T = int(input())
for test_case in range(1,T+1):
    n,m = map(int,input().split())
    p_list = list(range(n+1))
    for _ in range(m):
        a,b = map(int,input().split())
        union(a,b)

    result = set()
    for i in range(1,n+1):
        result.add(find(i))

    print(f'#{test_case} {len(result)}')