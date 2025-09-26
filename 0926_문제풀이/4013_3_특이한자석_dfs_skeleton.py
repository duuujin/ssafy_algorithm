import sys

sys.stdin = open("input.txt", "r")
from collections import deque


def dfs(mag, rot, visited):
    pass

T = int(input())
for test_case in range(1, T + 1):
    K = int(input())  # 회전 수
    N = 4
    ARROW_POS, RIGHT_POS, LEFT_POS = 0, 2, 6
    magnet_list = [deque(list(map(int, input().split()))) for _ in range(N)]
    rotate_info_list = [list(map(int, input().split())) for _ in range(K)]

    score_sum = 0  # 회득한 점수의 총 합을 저장할 변수
    for idx, magnet in enumerate(magnet_list):
        if not magnet[ARROW_POS]: continue
        score_sum += (2 ** idx)
    print(f"#{test_case} {score_sum}")
