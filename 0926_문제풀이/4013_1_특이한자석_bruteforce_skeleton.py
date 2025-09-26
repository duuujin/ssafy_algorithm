import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K = int(input())  # 회전 수
    # 주어진 자석이 4개이므로 4개의 입력값을 받음
    magnet_list = [list(map(int, input().split())) for _ in range(4)]
    # 회전 정보
    rotate_info_list = [list(map(int, input().split())) for _ in range(K)]
    score_sum = 0  # 회득한 점수의 총 합을 저장할 변수


    print(f"#{test_case} {score_sum}")
