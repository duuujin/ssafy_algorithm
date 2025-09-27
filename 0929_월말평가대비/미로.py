from collections import deque
dxy = [[0,1],[0,-1],[1,0],[-1,0]]

def bfs(miro):
    queue = deque()
    queue.append((1,1))
    visited = [[False] * (n+1) for _ in range(n)]
    visited[1][1] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx , ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and (visited[nx][ny] == False) and (arr[nx][ny] == 1 or arr[nx][ny] == 3):
                if arr[nx][ny] == 3:
                    return 1
                queue.append((nx,ny))
                visited[nx][ny] = True
    return 0

for _ in range(1,11):
    T = int(input())
    n = 16
    arr = [list(map(int,input().strip())) for _ in range(n)]
    result = bfs(arr)
    print(f'#{T} {result}')