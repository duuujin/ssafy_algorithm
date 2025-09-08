T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    dxy = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
    total_sum = 0
    start = 0

    for i in range(n):
        for j in range(n):
            start = arr[i][j]
            for dx,dy in dxy:
                ni = i + dx
                nj = j + dy
                if 0 <= ni < n and 0 <= nj < n :
                    start += arr[ni][nj]
                    total_sum = max(total_sum,start)
    print(total_sum)