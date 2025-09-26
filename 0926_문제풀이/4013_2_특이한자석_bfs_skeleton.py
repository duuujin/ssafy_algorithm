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
    # 아래와 같은 경우를 enum_type 대문자로 적는게 관례
    RIGHT_POS, LEFT_POS, ARROW_POS = 2, 6, 0

    # 주어진 회전정보를 큐에 집어넣고, 큐에서 꺼내면서 인접한 자석들을 다시 큐에 집어 넣는다.(조건은 방문하지 않았다는 조건)
    for rotate_info in rotate_info_list:
        magnet_num, rotate_dir = rotate_info
        queue = deque()
        queue.append([magnet_num - 1,rotate_dir])
        # 이미 방문했다(회전했다)한 자석은 큐에 넣지 않기 위해서(방문하지 않기 위해서) visited 변수 관리
        visited = [False] * N
        visited[magnet_num - 1] = True

        while queue:
            mag_idx, rotate = queue.popleft()

            # 가장 오른쪽 톱니바퀴가 아니라면, 무조건 오른쪽이랑 비교한다.
            if mag_idx != N-1:
                # 오른쪽이랑 비교하는 로직을 작성
                # 자성이 서로 다르다면 ! 큐에 추가한다. ( 조건은 방문한적이 없을것)
                if magnet_list[mag_idx][RIGHT_POS] != magnet_list[mag_idx + 1][LEFT_POS]:
                    if not visited[mag_idx + 1]:
                        queue.append([mag_idx + 1, -rotate])
                        visited[mag_idx + 1] = True

            # 가장 왼쪽 톱니바퀴가 아니라면, 무조건 왼쪽이랑 비교한다.
            if mag_idx != 0:
                if magnet_list[mag_idx][LEFT_POS] != magnet_list[mag_idx - 1][RIGHT_POS]:
                    if not visited[mag_idx - 1]:
                        queue.append([mag_idx - 1, -rotate])
                        visited[mag_idx - 1] = True

            # 근처에 있는 자석과 비교를 끝났고, 그 친구들을 큐에다가 다 집어넣었다.
            # 내가 할 건 ? -> 회전을 한다.
            magnet_list[mag_idx].rotate(rotate)

    # 점수를 얻어야한다
    # 1인 경우(S극)에만 점수에 넣는다
    for idx, magnet in enumerate(magnet_list):
        if not magnet[ARROW_POS]: continue # 화살표가 가르키는 자석이 N(0)이면 skip
        score_sum += (2 ** idx)

    print(f"#{test_case} {score_sum}")
