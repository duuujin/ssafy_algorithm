def find_set(x):
    if x != p_list[x]:
        p_list[x] = find_set(p_list[x])
    return p_list[x]

def union_set(x,y):
    px = find_set(x)
    py = find_set(y)

    if px != py:
        p_list[py] = px


T = int(input())
for test_case in range(1,T+1):
    n,m = map(int,input().split())
    p_list = list(range(n+1))
    rank = [0] * (n+1)
    answer = []
    for _ in range(m):
        e, a, b = map(int,input().split())
        if e == 0 :
            union_set(a,b)
        else:
            if find_set(a) == find_set(b):
                answer.append("1")
            else:
                answer.append("0")
    
    print(f'#{test_case} {"".join(answer)}')