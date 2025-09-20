T = 10
for test_case in range(1,T+1):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    def dfs(x,y,arr,visited):
        if arr[x][y] == 3:
            return True
        
        visited[x][y] = True
        
        for d in range(4):
            nx,ny = x+dx[d], y+dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if (arr[nx][ny] != 1) and visited[nx][ny] == False :
                    if dfs(nx,ny,arr,visited):
                        return True
        return False

    n = 16
    m = int(input())
    arr = [list(map(int,input().strip())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    result = 1 if dfs(1,1,arr,visited) else 0
    print(f'#{m} {result}')