import heapq, math
from collections import deque
dxy = [[0,1],[0,-1],[1,0],[-1,0]]
def bfs(arr, x, y,n):
    distance = [[math.inf] * n for _ in range(n)]
    distance[x][y] = 0
    hq = []
    heapq.heappush(hq, (0, (x,y)))

    while hq :
        d, (x,y) = heapq.heappop(hq)
        if x == n-1 and y == n-1:
            return d
        for dx,dy in dxy:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n:
                nd = d + arr[nx][ny]
                if nd < distance[nx][ny]:
                    distance[nx][ny] = nd
                    heapq.heappush(hq, (nd, (nx,ny)))


T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().strip())) for _ in range(n)]

    result = bfs(arr,0,0,n)
    print(f'#{test_case} {result}')