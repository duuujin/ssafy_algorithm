"""
미로 같은 문제는 일반적으로 BFS로 푸는게 맞음.
미로 문제를 DFS로 푼다?
만약에 모든 길이 이동 가능한 미로 -> 시간복잡도 증가.

그런데도 DFS로 접근해야하는 경우
1) DFS: 
    - 재귀적으로 구현 할 때, 누적해서 가져가는 값(목표로 하는 값) , 파라미터로 준다.
    - 목적지까지 도달하는 '경로'에서 특정 조건을 구해야 하는 경우
2) BFS: 
    - 최단거리 -> 중간에 목적 좌표 만나면 종료 
    - 최단 목표 도달하는 과정을 알기 어려움 -> 결과 중심

"""
dxy = [[1,0],[-1,0],[0,1],[0,-1]]
def dfs(x, y, count):
    global min_count

    # 종료 조건 x,y가 n-1,m-1 에 도달하면 종료, 이때까지의 이동거리가 최소 이동거리보다 작으면 갱신
    if x == N-1 and y == M-1:
        min_count = min(count,min_count)
        return
    
    for dx,dy in dxy:
        nx , ny = x + dx, y + dy
        # 범위를 벗어나거나, 방문한적이 있거나, 길이 아니면 skip
        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue

        # 방문한 적이 있으면 skip
        if visited[nx][ny] : continue

        if not road[nx][ny]: continue

        # 본인 방문처리하고, 다음좌표 +1 다시 DFS 호출한다.
        visited[nx][ny] = True
        dfs(nx,ny,count+1)
        visited[nx][ny] = False


# 입력 받기
N, M = map(int, input().split())
road = [list(map(int, input())) for _ in range(N)]

# 방문 처리를 위한 변수가 필요함.
visited = [[False] * N for _ in range(N)]
min_count = float('INF')
visited[0][0] = True

# 파라미터로 뭘 넘길까?
# 1. 종료조건 (좌표 -> 목적좌표에 도달)
# 2. 얻으려고 하는 누적 값 -> 이동한 거리(움직인 횟수)
dfs(0,0,0)
