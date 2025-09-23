def find_set(x):
    if x != p_list[x]:
        p_list[x] = find_set(p_list[x])
    return p_list[x]

def union(x,y):
    px = find_set(x)
    py = find_set(y)
    if px != py:
        p_list[py] = px

T = int(input())
for test_case in range(1,T+1):
    N,M = map(int,input().split())
    p_list = list(range(N+1))
    for _ in range(M):
        a,b = map(int,input().split())
        union(a,b)
    
    result = set()
    for i in range(1,N+1):
        result.add(find_set(i))

    print(f'#{test_case} {len(result)}')