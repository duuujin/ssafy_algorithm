def inord(n):
    if n <= N:
        inord(n * 2)
        inord(n * 2 + 1)
        ans.append(lst[n])

T = 10
for test_case in range(1,T+1):
    N = int(input())
    lst = [0] * (N+1)
    for i in range(1,N+1):
        tlist = input().split()
        lst[i] = tlist[1]
    ans = []
    inord(1)
    print(f'#{test_case} {"".join(ans)}')


