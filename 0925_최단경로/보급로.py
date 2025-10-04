<<<<<<< HEAD
import heapq
from collections import deque
def bfs(arr, x, y)
    
=======
import math, heapq
dxy = [[0,1],[0,-1],[1,0],[-1,0]]

def bfs(arr):
    distance = [[math.inf] * n for _ in range(n)]
    hq =[]
    distance[0][0] = 0
    heapq.heappush(hq, (0,0,0))

    while hq:
        dist, x, y = heapq.heappop(hq)
        if x == n-1 and y == n-1:
            return dist
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n :
                nextdist = dist + arr[nx][ny]
                if nextdist < distance[nx][ny]:
                    distance[nx][ny] = nextdist
                    heapq.heappush(hq, (nextdist,nx,ny))

>>>>>>> 485c0c243f167de6e4c6f277a98ebbab412eba7a

T = int(input())
for test_case in range(1,T+1):
    n = int(input())
<<<<<<< HEAD
    map = [list(map(int,input().split())) for _ in range(n)]

    result = bfs(map,0,0)
=======
    arr = [list(map(int,input())) for _ in range(n)]
    

    total_cnt = bfs(arr)
    print(f'#{test_case} {total_cnt}')
>>>>>>> 485c0c243f167de6e4c6f277a98ebbab412eba7a
