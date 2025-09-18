import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/ssafy_algorithm/ssafy_algorithm/0918_BFS/miro.txt','r')
from collections import deque
T = 10
for test_caes in range(1,T+1):

    def bfs(arr):
        queue = deque()
        queue.append((1,1))

        visited = [[False] * 16 for _ in range(16)]
        visited[1][1] = True

        while queue:
            x,y = queue.popleft()
            for dx,dy in dxy:
                nx , ny = x+dx, y+dy
                if 0 <= nx < 16 and 0 <= ny < 16 and not visited[nx][ny] and (arr[nx][ny] == 0 or arr[nx][ny] == 3):
                    if arr[nx][ny] == 3:
                        return 1
                    queue.append((nx,ny))
                    visited[nx][ny] = True
        return 0

    dxy = [[0,1],[0,-1],[1,0],[-1,0]]
    n = int(input())
    arr = [list(map(int,input().strip())) for _ in range(16)]
    result = bfs(arr)
    print(f'#{test_caes} {result}')
        
