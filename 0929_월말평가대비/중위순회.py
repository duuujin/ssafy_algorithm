def innord(n):
    if n <= N:
        innord(n*2)
        ans.append(lst[n])
        innord(n*2+1)

for test_case in range(1,11):
    N = int(input())
    lst = [0] * (N+1)
    for i in range(1,N+1):
        tlist = input().split()
        lst[i] = tlist[1]
    ans = []
    innord(1)
    print(f'#{test_case} {"".join(ans)}')