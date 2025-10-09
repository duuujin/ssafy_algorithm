import heapq, math
dxy = [[0,1],[0,-1],[1,0],[-1,0]]
def bfs(x,y,n):
    distance = [[math.inf] * n for _ in range(n)]
    distance[x][y] = 0
    min_heap = []
    heapq.heappush(min_heap , (0, (x,y)))

    while min_heap:
        d, (cx, cy) = heapq.heappop(min_heap)
        if distance[cx][cy] < d : continue
        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n :
                nd = d + 1
                if arr[nx][ny] > arr[cx][cy]:
                    nd += arr[nx][ny] - arr[cx][cy]
                if nd < distance[nx][ny]:
                    distance[nx][ny] = nd
                    heapq.heappush(min_heap, (nd, (nx,ny)))
    return distance[n-1][n-1]

T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    start_x = 0
    start_y = 0
    result = bfs(start_x,start_y,n)
    print(f'#{test_case} {result}')