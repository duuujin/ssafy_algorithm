import heapq,math
dxy = [[0,1],[0,-1],[1,0],[-1,0]]
# 출발은 항상 맨 왼쪽 위, 도착은 맨 오른쪽 아래 상하좌우이동
# 이동시 기본 카운트 1씩 증가, 높이가 더 높으면 , 높은 곳 - 현재 높이 값을 추가
# 시작은 (0,0) 도착은 (n-1, n-1)
def dijk(n, arr, start, start1):
    distance = [[math.inf] * n for _ in range(n)]
    distance[start][start1] = 0
    min_heap = []
    heapq.heappush(min_heap, (0, (start,start1)))

    while min_heap:
        d, (x, y) = heapq.heappop(min_heap)
        if distance[x][y] < d: continue
        for dx,dy in dxy:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n:
                nd = d + 1
                if board[nx][ny] > board[x][y]:
                    nd += board[nx][ny] - board[x][y]
                if nd < distance[nx][ny] :
                    distance[nx][ny] = nd
                    heapq.heappush(min_heap, (nd, (nx,ny)))
    return distance[n-1][n-1]


T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n)]

    start_x = 0
    start_y = 0
    res = dijk(n, board, start_x, start_y)
    print(f'#{test_case} {res}')