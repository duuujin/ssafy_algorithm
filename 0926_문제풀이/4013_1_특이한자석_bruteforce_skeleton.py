import sys
sys.stdin = open("input.txt", "r")
from collections import deque
"""
하드코딩 + 확장성 x , 유연하지도 않은 코드로 구현
-> 그렇다고 잘못된건 아님.

첫 번째로 푸는 방식
- 자석의 회전 방향을 모두 고려한 뒤에, 회전 방향에 따라서 한 번에 회전하고 점수를 획득하는 방식
"""
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K = int(input())  # 회전 수
    # 주어진 자석이 4개이므로 4개의 입력값을 받음
    magnet_list = [deque(list(map(int, input().split()))) for _ in range(4)]
    # 회전 정보
    rotate_info_list = [list(map(int, input().split())) for _ in range(K)]
    score_sum = 0  # 회득한 점수의 총 합을 저장할 변수
    
    def rotate_magnet(mag, rot, visited):
        # 이미 방문한 적 있으면, 재귀함수를 진행하지 않음
        if visited[mag] != 0: return
        
        # 방문한 적이 없기 때문에, 이제 해당 자석을 회전시켜야하는 방향에 따라서 회전 예정 정보 저장
        visited[mag] = rot

        # 1번 자석인 경우 ( 오른쪽 자석 비교)
        if mag == 0:
            # 현재 자석[2]과 오른쪽 자석[6] 서로 비교
            if magnet_list[mag][2] != magnet_list[mag+1][6]:
                rotate_magnet(mag + 1, -rot, visited)
        # 4번 자석인 경우 ( 왼쪽 자석 비교)
        elif mag == 3:
            # 현재 자석[6]과 왼쪽 자석[2] 서로 비교
            if magnet_list[mag][6] != magnet_list[mag-1][2]:
                rotate_magnet(mag - 1, -rot, visited)
        # 2번, 3번 자석의 경우 ( 양쪽 자석 비교)
        else:
            # 본인 자석[2]과 오른쪽 자석[6]
            if magnet_list[mag][2] != magnet_list[mag + 1][6]:
                rotate_magnet(mag+1, -rot, visited)

            # 본인 자석[6]과 왼쪽 자석[2] 비교
            if magnet_list[mag][6] != magnet_list[mag - 1][2]:
                rotate_magnet(mag-1, -rot, visited)

        

    # 주어진 회전 정보 (rotate_info_list)에 따라서 자석을 회전한다.
    for rotate_info in rotate_info_list:
        # marnet_num : 마그넷 번호
        # rotate_dir : 회전방향 ( 1: 시계방향, -1: 반시계방향)
        magnet_num, rotate_dir = rotate_info

        # 각 자석이 어떤 방향으로 회전해야할 지 알려주는 변수 + 이미 회전을 했는지를 확인하는 변수
        # 아래에 작성할 회전 함수(재귀함수)가 동작하고 나서는 visited에 4개의 자석이 회전해야 하는 방향이 저장된다.
        visited = [0] * 4

        # 번호에 해당하는 자석이 어느 방향으로 돌아가는지 확인하는 함수
        # magnet_num: 어떤 자석인지 나타내는 변수
        # rotate_dir: 해당 자석이 회전해야하는 방향
        # visited : 방문 여부 확인 + 어떤 방향으로 돌 예정인지 검사할 변수
        rotate_magnet(magnet_num - 1, rotate_dir, visited)

        # i : 회전 시켜야하는 자석의 번호
        # v : 회전 시켜야하는 방향
        for i, v in enumerate(visited):
            # if v == 1:  # 시게 방향으로 회전
            #     pop_data = magnet_list[i].pop()
            #     magnet_list[i].appendleft(pop_data)
            # elif v == -1:   # 반시계 방향으로 회전
            #     pop_data = magnet_list[i].popleft()
            #     magnet_list[i].append(pop_data)
            magnet_list[i].rotate(v)

        
        # 결과를 계산
        # 4개의 자석에 대해서 빨간색 화살표의 위치(0)에 해당하는 애들이 S(1)의 경우에 점수 추가
    score_list = [1,2,4,8]
    for i in range(4):  # i는 자석의 인덱스 번호
        if magnet_list[i][0] == 1:  # 빨간색 화살표의 위치가 S극이면
            score_sum += score_list[i]

    print(f"#{test_case} {score_sum}")
