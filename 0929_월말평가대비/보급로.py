from collections import deque

# dxy = [[0,1],[0,-1],[1,0],[-1,0]]

# def bfs(arr,n):
#     queue = deque()
#     queue.append((0,0))
#     distance = [[float('inf')] * n for _ in range(n)]
#     distance[0][0] = 0

#     while queue:
#         x, y = queue.popleft()
#         for dx, dy in dxy:
#             nx , ny = x + dx, y + dy
#             if 0 <= nx < n and 0 <= ny < n :
#                 min_money = distance[x][y] + arr[nx][ny]
#                 if min_money < distance[nx][ny]:
#                     distance[nx][ny] = min_money
#                     queue.append((nx,ny))
#     return distance[n-1][n-1]

# T = int(input())
# for test_case in range(1,T+1):
#     n = int(input())
#     arr = [list(map(int,input().strip())) for _ in range(n)]
#     result = bfs(arr,n)
#     print(f'#{test_case} {result}')
import heapq
dxy = [[0,1],[0,-1],[1,0],[-1,0]]

def distra(arr, n):
    distance = [[float('inf')] * n for _ in range(n)]
    hq = []
    distance[0][0] = 0
    heapq.heappush(hq, (0,0,0))

    while hq:
        dis , x, y = heapq.heappop(hq)
        if x == n -1 and y == n-1 :
            return dis
        for dx, dy in dxy:
            nx , ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                nd = dis + arr[nx][ny]
                if nd < distance[nx][ny] :
                    distance[nx][ny] = nd
                    heapq.heappush(hq, (nd,nx,ny))



T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().strip())) for _ in range(n)]
    cnt = 0
    result = distra(arr,n)
    print(f'#{test_case} {result}')