import sys
sys.stdin = open("4828_input.txt", "r")

T = int(input())  # 테스트 케이스 개수

for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())  # 최대 이동 거리, 종점, 충전소 개수
    charge_stations = set(map(int, input().split()))  # 충전소 위치 (set 사용으로 탐색 속도 향상)

    charge_count = 0  # 충전 횟수
    position = 0  # 현재 위치

    while position + K < N:  # 종점 도착 전까지 반복
        next_position = position + K  # 최대 이동 가능한 위치
        
        while next_position > position and next_position not in charge_stations:
            next_position -= 1  # 충전소를 찾을 때까지 한 칸씩 뒤로 이동

        if next_position == position:  # 더 이상 충전소를 찾을 수 없으면 도착 불가능
            charge_count = 0
            break

        position = next_position  # 충전소에서 충전 후 이동
        charge_count += 1

    print(f"#{test_case} {charge_count}")