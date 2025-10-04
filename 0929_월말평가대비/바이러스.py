from collections import deque
dxy = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]

def bfs(arr,x,y):
    queue = deque()
    queue.append((x,y))
    arr[x][y] = "0"
    count = 1

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in dxy:
            nx , ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != "0":
                queue.append((nx,ny))
                arr[nx][ny] = "0"
                count += 1
    return count

T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    arr = [list(input().split()) for _ in range(n)]
    max_size = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == "0":
                continue
            max_size = max(max_size, bfs(arr,i,j))

    print(f'#{test_case} {max_size}')
