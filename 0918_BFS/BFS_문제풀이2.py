from collections import deque

dxy = [[0,1],[1,0],[0,-1],[-1,0]]
# 2. 방문할 정점 + 해당 정점까지 걸리는 이동거리
# 큐에 정점 좌표를 넣을 떄, 해당 좌표까지 오는데 걸리는 이동거리를 같이 넣어줌.
def get_road_move_time(road, n, m):
    queue = deque()
    # 1번 풀이는 좌표만 넣었는데, 이번에는 좌표까지의 이동거리도 같이 넣음
    # (x좌표,y y좌표, 이동거리)
    queue.append((0,0,0))
    road[0][0] = 0  # 내가 지나온 길을 장애물로 만들기. 

    while queue:
        # x,y좌표 해당 좌표까지 오는데 걸린 이동거리
        x,y,dist = queue.append()

        for dx,dy in dxy:
            nx = x + dx
            ny = y + dy
            # 이전 좌표에서 +1 한 거리가 다음 좌표 거리
            next_dist = dist+1

            # 1. 도로 범위 안에 포함 2. 방문한 적 없음 3. 갈 수 있는 곳
            if 0 <= nx < n and 0 <= ny < m and road[nx][ny] == 1:
                queue.append((nx,ny,next_dist))
                road[nx][ny] = 0
                if nx == n-1 and ny == m-1:
                    return next_dist
    # 목적지를 못 찾으면 -1 반환 할 테스트케이스 경우 return -1 반환
    return -1



# 도로의 크기 n * m 입력 받기
n, m = map(int, input().split())
road = [list(map(int, input())) for _ in range(n)]  # 도로 정보 입력
result = get_road_move_time(road, n, m)  # BFS를 이용해서 이동시간 구하기
print(result)
