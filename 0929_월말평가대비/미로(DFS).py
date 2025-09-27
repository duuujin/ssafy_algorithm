dxy = [[0,1],[0,-1],[1,0],[-1,0]]

def dfs(x, y):
    visited[x][y] = True
    if miro[x][y] == 3:
        return True
    
    for dx , dy in dxy:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False :
            if miro[nx][ny] == 1: continue
            if dfs(nx,ny):
                return True
    return False

for _ in range(1,11):
    T = int(input())
    n = 16
    miro = [list(map(int,input().strip())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    result = 1 if dfs(1,1) else 0
    print(f'#{T} {result}')