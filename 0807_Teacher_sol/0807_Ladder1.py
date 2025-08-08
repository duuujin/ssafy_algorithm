# 아래, 우, 좌 => 순서 상관 x
dxy = [[1, 0], [0, 1], [0, -1]]

# 시작점에서 끝까지 내려가서 "2"에 걸맞는 시작점인지 확인하는 함수
# x, y 는 시작점 !
def search_ladder(x, y):
    # 주의사항
    # 왼, 오른쪽 사다리 검사를 할 때, 이미 왔던 길을 가는 경우도 있다.
    # 방문 여부를 체크하는 복사본을 하나 만들거에요
    visited = [[0] * N for _ in range(N)]  # N * N 사이즈로 방문 체크용 배열을 만들어준다.
    visited[x][y] = 1  # 초기에 시작하는 위치에 방문했다고 치고 간다.

    # 저 델타탐색을 이용해서 아래로 쭉 내려갈거에요
    # 언제까지? x == 99가 될때까지 내려갈거에요. (N-1)
    # x 는 시작점이고, 행을 의미해요
    while x != 99:  # 끝에 도달하지 않았으면, 아래 로직을 계속 반복한다.
        # 3방향을 델타 탐색 시작하자 .
        for dx, dy in dxy:
            # 다음에 이동할 좌표
            nx, ny = x + dx, y + dy

            # 이동하기 위한 조건
            """
            1. 범위 안에 들어있어야 한다.  ( 0 <= x < N and 0 <= y < N)
            2. 사다리가 놓여있어야 한다.  ( data[x][y] => 1
            3. 방문한 적이 없어야 한다. ( visited[x][y] == 0 인곳만 갈수있다 ) 
            """
            if 0 <= nx < N and 0 <= ny < N and data[nx][ny] and not visited[nx][ny]:
                # 여기 안에 들어왔따는 건 다음 좌표로 이동해도 된다는거에요 .
                x, y = nx, ny
                visited[nx][ny] = 1

    # x => 무조건 99 에 해당한다.
    return data[x][y] == 2  # True를 반환하겠죠.. 아님ㄴ False 반환하겠죠



for _ in range(1, 11):
    tc = int(input())
    N = 100
    result = -1  # 못 찾는 경우 -1로 세팅하고, 찾으면 시작 인덱스를 설정한다.
    data = [list(map(int, input().split())) for _ in range(N)]

    # 출발점이 1인 지점에서 search_leadder() 함수를 실행할 거다.
    for j in range(N):
        if data[0][j] == 1:  # 1인 곳은 사다리가 놓여져 있으므로, 사다리타기 시작!
            if search_ladder(0, j):  # 마지막에 도달한 장소가 2인 경우에는 True, 2가 아니면 False
                # 여기에 들어왔따는 건 올바른 시작점을 찾았다는 것 => 그 시작점은 "j"
                result = j
                break

    print(f"#{tc} {result}")
