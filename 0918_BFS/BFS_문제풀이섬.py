from collections import deque

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def find_island(island, x, y):
    queue = deque()

    # queue에 정점을 넣으면, 무조건 방문처리
    queue.append((x, y))
    island[x][y] = 0

    while queue:
        cx, cy = queue.popleft()

        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy

            # 격자 안이여야 함.
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 육지여야한다.
            if island[nx][ny] == 0:
                continue

            queue.append((nx, ny))
            island[nx][ny] = 0


n, m = map(int, input().split())  # 섬의 크기 입력
arr = [list(map(int, input())) for _ in range(n)]  # 섬의 상태 입력 받기
island_cnt = 0  # 섬의 개수

# 그래프, 모든 정점이 연결되어 있다는 보장이 없음.
# 모든 정점에서 bfs를 실행해야함.
for i in range(n):
    for j in range(m):
        # 바다에서 시작하면 안됨 -> 육지에서만 실행
        # 바다이면 skip
        if arr[i][j] == 0:
            continue

        find_island(arr, i, j)
        island_cnt += 1

print(island_cnt)  # 섬의 개수 출력
