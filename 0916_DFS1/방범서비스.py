dxy = [[0,1],[0,-1],[1,0],[-1,0]]
T = int(input())
for test_case in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    def dfs(x,y,depth,k,visited):
        if depth >= k:
            return
        if not (0 <= x < N and 0<= y < N):
            return
        if visited[x][y] == True:
            return
        
        visited[x][y] = True

        for dx, dy in dxy:
            nx = x+dx
            ny = y+dy
            dfs(nx,ny,depth+1,k,visited)

# ---------- 전부 이상한 코드들

    answer = 0
    for i in range(N):
        for j in range(N):
            for k in range(1,N+2):
                visited = [[False] * N for _ in range(N)]
                dfs(i,j,0,k,visited)
                

                house = 0
                for m in range(N):
                    for n in range(N):
                        if visited[i][j] == True and arr[i][j] == 1:
                            house += 1

                cost = k * k + (k-1) * (k-1)

                if house * M >= cost:
                    answer = max(house,answer)
    print(f'#{test_case} {answer}')