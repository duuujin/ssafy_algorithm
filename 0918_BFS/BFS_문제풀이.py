# 1. 전체 공간을 복사하고, 각 공간의 좌표마다, 시작지점에서 얼마나 떨어져 있는지 확인
# 장점:  모든 목적지의 최단 거리를 알 수 있다. (시작지점 바뀌면, 의미없음)
# 단점: 메모리 2배 차지

from collections import deque
dxy = [[1,0],[0,1],[-1,0],[0,-1]]

def get_road_move_time(road, n, m):
    queue = deque()
    # queue에다가 시작지점을 넣어야한다.
    # 지금 문제의 목표가 [1,1] -> [N,M]
    # [0,0] -> [n-1,m-1]
    # 좌표를 튜플 형태로 넣엇는데, 리스트 가능, 튜플:변경 불가
    queue.append((0,0))
    
    # 1. 복사하는 과정 -> 모든 좌표에 도달하는 최단거리를 저장할 변수
    # 2. 방문처리를 진행할 변수
    # 이렇게 두가지 역할을 한다.
    # -1이면, 아직 최단거리가 갱신 되지 않았다는 것. -> 방문 한 적이 없다. 
    # -1이 아니라는건, 최단거리가 갱신, 방문한적이 있음.
    # -1 이 의미하는건 없다. ..-> 어떤 걸 하든 상관없음.
    distance = [[-1] * m for _ in range(n)]
    distance[0][0] = 0

    while queue:
        x,y = queue.popleft()
        # x,y를 기준으로 갈 수 있는 곳을 queue에다가 집어넣음.
        for dx,dy in dxy:
            nx, ny = x+dx, y+dy # 현재 위치x,y에서 방향에 따라 이동하는 좌표 확인

            # 이동할 수 있는 조건
            # 1. 지도 안에 포함 될 것. (범위)
            # 2. 방문한 적이 없을 것.(distance가 -1 인 곳)
            # 3. 갈 수 있는 곳(road = 1) 인 곳
            if 0 <= nx < n and 0 <= ny < m and distance[nx][ny] == -1 and road[nx][ny] == 1:
                # 조건을 통과했다는 건 갈 수 있는 곳.
                queue.append(nx,ny)
                # 방문처리 해줘야함.
                # 인접하기 때문에, 전 좌표의 거리 + 1
                distance[nx][ny] = distance[x][y] + 1
                
                # 우리 목표를 잊으면 안됨. (n-1,m-1)인지 확인해야 함
                if nx == n-1 and ny == m-1:
                    return distance[nx][ny]
                


# 도로의 크기 n * m 입력 받기
n, m = map(int, input().split())
# 도로 정보 입력
road = [list(map(int, input())) for _ in range(n)]

# BFS를 이용해서 이동시간 구하기
result = get_road_move_time(road, n, m)
print(result)
