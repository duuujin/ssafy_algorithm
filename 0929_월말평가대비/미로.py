from collections import deque
dxy = [[0,1],[0,-1],[1,0],[-1,0]]

def bfs(miro):
    queue = deque()
    queue.append((1,1))
    visited = [[False] * 16 for _ in range(16)]
    visited[1][1] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < 16 and 0 <= ny < 16 and visited[nx][ny] == False and (miro[nx][ny] == 0 or miro[nx][ny] ==3):
                if miro[nx][ny] == 3:
                    return 1
                queue.append((nx,ny))
                visited[nx][ny] = True
    return 0


for test_case in range(1,11):
    T = int(input())
    miro = [list(map(int,input().strip())) for _ in range(16)]

    result = bfs(miro)
    print(f'#{test_case} {result}')