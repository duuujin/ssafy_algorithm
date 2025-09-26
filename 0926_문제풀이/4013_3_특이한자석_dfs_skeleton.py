import sys

sys.stdin = open("input.txt", "r")
from collections import deque


def dfs(mag_idx, rot, visited):
    if mag_idx != N - 1:
        # 오른쪽이랑 비교하는 로직을 작성
        # 자성이 서로 다르다면 ! 큐에 추가한다. ( 조건은 방문한적이 없을것)
        if magnet_list[mag_idx][RIGHT_POS] != magnet_list[mag_idx + 1][LEFT_POS]:
            if not visited[mag_idx + 1]:
                visited[mag_idx + 1] = True
                dfs(mag_idx + 1 , -rot, visited)

    # 가장 왼쪽 톱니바퀴가 아니라면, 무조건 왼쪽이랑 비교한다.
    if mag_idx != 0:
        if magnet_list[mag_idx][LEFT_POS] != magnet_list[mag_idx - 1][RIGHT_POS]:
            if not visited[mag_idx - 1]:
                visited[mag_idx - 1] = True
                dfs(mag_idx - 1, -rot, visited)

    magnet_list[mag_idx].rotate(rot)

T = int(input())
for test_case in range(1, T + 1):
    K = int(input())  # 회전 수
    N = 4
    ARROW_POS, RIGHT_POS, LEFT_POS = 0, 2, 6
    magnet_list = [deque(list(map(int, input().split()))) for _ in range(N)]
    rotate_info_list = [list(map(int, input().split())) for _ in range(K)]

    for rotate_info in rotate_info_list:
        magnet_num, rotate_dir = rotate_info
        visited = [False] * N

        dfs(magnet_num - 1, rotate_dir, visited)

    print(f"#{test_case}")
