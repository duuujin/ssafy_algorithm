import sys
sys.stdin = open("input.txt", "r")
from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    K = int(input())  # 회전 수
    N = 4  # 자석의 개수를 변수로 활용
    magnet_list = [deque(list(map(int, input().split()))) for _ in range(N)]
    rotate_info_list = [list(map(int, input().split())) for _ in range(K)]
    score_sum = 0  # 회득한 점수의 총 합을 저장할 변수

    print(f"#{test_case} {score_sum}")
