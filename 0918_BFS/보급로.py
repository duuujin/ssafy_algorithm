# -----------------유신형님 티칭----------------
import heapq, time, sys
sys.stdin = open("C:/Users/enwls/Desktop/ssafy_algorithm/ssafy_algorithm/0918_BFS/input.txt", "r")
dxy = [[0,1],[0,-1],[1,0],[-1,0]]
start = time.perf_counter()
T = int(input())
for test_case in range(1,T+1):

    def bfs(arr,cnt):
        distance = [[10**9] * n for _ in range(n)]
        hq = []
        distance[0][0] = 0
        heapq.heappush(hq, (0, 0, 0))
        
        while hq:
            d,x,y = heapq.heappop(hq)
            if x == n - 1 and y == n - 1:
                return d
            for dx,dy in dxy:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < n:
                    nd = d + arr[nx][ny]
                    if nd < distance[nx][ny]:
                        distance[nx][ny] = nd  
                        heapq.heappush(hq, (nd, nx, ny))
        # return distance[n-1][n-1]

    n = int(input())
    arr = [list(map(int,input())) for _ in range(n)]
    cnt = 0
    total_cnt = bfs(arr, cnt)
    print(f'#{test_case} {total_cnt}')
end = time.perf_counter()
print("실행 시간:", end - start, "초")
print("-------------------------------------------------")
# -----------------유신형님 티칭----------------

# ---------GPT 티칭 ---------------------------
import sys
sys.stdin = open("C:/Users/enwls/Desktop/ssafy_algorithm/ssafy_algorithm/0918_BFS/input.txt", "r")
from collections import deque
dxy = [[0,1],[0,-1],[1,0],[-1,0]]
start = time.perf_counter()
T = int(input())
for test_case in range(1, T+1):

    def bfs(arr, cnt):
        INF = 10**9
        dist = [[INF] * n for _ in range(n)]   # 각 칸까지의 최소 복구시간
        in_queue = [[False] * n for _ in range(n)]
        queue = deque()

        dist[0][0] = 0
        queue.append((0,0))
        in_queue[0][0] = True

        while queue:
            x, y = queue.popleft()
            in_queue[x][y] = False
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    nd = dist[x][y] + arr[nx][ny]
                    if nd < dist[nx][ny]:
                        dist[nx][ny] = nd
                        if not in_queue[nx][ny]:
                            queue.append((nx,ny))
                            in_queue[nx][ny] = True
        return dist[n-1][n-1]

    n = int(input())
    arr = [list(map(int, input().strip())) for _ in range(n)]
    cnt = 0
    total_cnt = bfs(arr, cnt)
    print(f"#{test_case} {total_cnt}")
end = time.perf_counter()
print("실행 시간:", end - start, "초")
print("-------------------------------------------------")
# ---------GPT 티칭 ---------------------------

# ---------내가 풀어볼 거 ---------------------------
import sys
sys.stdin = open("C:/Users/enwls/Desktop/ssafy_algorithm/ssafy_algorithm/0918_BFS/input.txt", "r")
from collections import deque
start = time.perf_counter()
T = int(input())
for test_case in range(1,T+1):
    dxy = [[0,1],[0,-1],[1,0],[-1,0]]
    def bfs(arr,n):
        distance = [[float('INF')] * n for _ in range(n)]
        queue = deque()
        queue.append((0,0))
        distance[0][0] = 0

        while queue:
            x,y = queue.popleft()
            for dx,dy in dxy:
                nx,ny = x+dx, y+dy

                if 0 <= nx < n and 0 <= ny < n:
                    min_money = distance[x][y] + arr[nx][ny]
                    if distance[nx][ny] > min_money:
                        distance[nx][ny] = min_money
                        queue.append((nx,ny))
        return distance[n-1][n-1]


    n = int(input())
    arr = [list(map(int,input().strip())) for _ in range(n)]
    result = bfs(arr,n)
    print(f'#{test_case} {result}')
end = time.perf_counter()
print("실행 시간:", end - start, "초")
# ----------------------------------------------------