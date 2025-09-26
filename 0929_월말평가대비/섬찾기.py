from collections import deque
dxy = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]


def bfs(island,x, y):
    queue = deque()
    queue.append((x,y))
    island[x][y] = 0

    while queue:
        cx, cy = queue.popleft()

        for dx,dy in dxy:
            nx , ny = cx+dx, cy+dy

            if not (0 <= nx < n and 0 <= ny < m ):
                continue
            
            if island[nx][ny] == 0:
                continue

            queue.append((nx,ny))
            island[nx][ny] = 0


n,m = map(int,input().split())
arr = [list(map(int,input())) for _ in range(n)]
total_cnt = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 : continue

        bfs(arr,i,j)
        total_cnt += 1

print(total_cnt)