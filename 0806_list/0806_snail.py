N = 5 
matrix = [
    [9, 20, 2, 18, 11],
    [19, 1, 25, 3, 21],
    [8, 24, 10, 17, 7],
    [15, 4, 16, 5, 6],
    [12, 13, 22, 23, 14]
]
# 2차원 리스트를 1차원리스트로 바꾸고 ,정렬한다
# [1,2,3,4,5, ..., 24, 25 ]
sorted_list = []
for row in matrix:  # row => 행을 의미
    for num in row:  # col => 고정된 행의 열을 의미합니다.
        sorted_list.append(num)

sorted_list.sort()

# 빈 5*5 행렬을 만들어야 한다.
# [0, 0,0,0,0] 이거를 하나 만들고, 이걸 N 번반복해서 2차원 리스트를 만들겠다.
result = [[0] * N for _ in range(N)]
print(result)

# 달팽이의 운동 방향 ( 오른쪽 -> 아래 -> 왼쪽 -> 위)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0
direction = 0

# 1, 2, ,3 ,4 , ...
# 위의 값을 순회하면서 우리가 만든 result 값에다가 채워넣을거다.
for value in sorted_list:
    result[x][y] = value  # 값을 채웠다.
    # 다음 좌표로 이동한다.
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 조건은 벽에 부딪친다(범위를 벗어났ㅇ거나)
    # 이미 값이 채워져있는 경우에는 방향을 바꾼다.
    # 범위 안에 없거나... 채워져있는 곳으로 가는 경우에는
    # 방향을 바꿔야 한다.
    if not( 0 <= nx < N and 0 <= ny < N and result[nx][ny] == 0):
        direction = (direction + 1) % 4  # 다음의 방향으로 바꿀 수 있다.
        nx, ny = x + dx[direction], y + dy[direction]

    # 현재 좌표를 이동할 좌표로 갱신해준다. ( 갈 수 있는 좌표기 때문에 갱신해도 됨)
    x, y = nx, ny
print(result)
