from collections import deque
import math,heapq
dxy = [[0,1],[0,-1],[1,0],[-1,0]]

def bfs(miro,n,sx,sy):
    hq = []
    heapq.heappush(hq, (0,(sx,sy)))
    distance = [[math.inf] * n for _ in range(n)]
    distance[sx][sy] = 0

    while hq:
        di, (x,y) = heapq.heappop(hq)
        if distance[x][y] < di : continue
        for dx,dy in dxy:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n:
                nd = di + 1
                if miro[nx][ny] > miro[x][y]:
                    nd += miro[nx][ny] - miro[x][y]
                if nd < distance[nx][ny]:
                    distance[nx][ny] = nd
                    heapq.heappush(hq, (nd, (nx,ny)))
    return distance[n-1][n-1]

T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    start_x = 0
    start_y = 0
    result = bfs(arr,n,start_x,start_y)
    print(f'#{test_case} {result}')