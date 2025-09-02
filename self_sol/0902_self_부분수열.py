from itertools import combinations,product,permutations
T = int(input())
for test_case in range(1,T+1):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    cnt = 0
    for i in range(n):
        for idx in combinations(arr,i):
            if sum(idx) == k:
                cnt += 1
    print(f'#{test_case} {cnt}')
    