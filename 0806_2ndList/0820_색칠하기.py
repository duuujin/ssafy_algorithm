T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    arr = [[0]*10 for _ in range(10)]
    total_cnt = 0
    for _ in range(n):
        pa1,pa2,pa3,pa4,c = map(int,input().split())
        for i in range(pa1,pa3+1):
            for j in range(pa2,pa4+1):
                if arr[i][j] != c :
                    arr[i][j] += c
    
    for ii in range(10):
        for jj in range(10):
            if arr[ii][jj] == 3:
                total_cnt += 1
        

    print(f'#{test_case} {total_cnt}')