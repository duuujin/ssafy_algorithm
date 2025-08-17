T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input())) for _ in range(n)]

    mid = n // 2
    total_sum = 0
    
    for i in range(n):
        dist = abs(mid - i)
        start = dist
        end = n - dist
        total_sum += sum(arr[i][start:end])

    print(f'#{test_case} {total_sum}')