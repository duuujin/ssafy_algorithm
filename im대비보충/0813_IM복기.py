T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    dxy = [[0,1],[0,-1],[1,0],[-1,0]]
    

    # for i in range(n):
    #     for j in range(n):
    #         max_count = 0
    #         c_count = 1
    #         current = arr[i][j]
    #         for dx,dy in dxy:
    #             ni = i + dx
    #             nj = j + dy
    #             if 0 <= ni < n and 0 <= nj < n :
    #                 current = arr[ni][nj]
    #                 c_count += 1
    #             max_count = max(c_count,max_count)
                        
    #                 # if arr[i][j] > arr[ni][nj] > arr[i+1][j+0]:
    #                 #     current = arr[ni][nj]
    #                 #     c_count += 1
    #                 # max_count = max(c_count,max_count)
            
                
    # print(f'#{test_case} {max_count}')
    # ----------------------------------------------------------------

    # while True: