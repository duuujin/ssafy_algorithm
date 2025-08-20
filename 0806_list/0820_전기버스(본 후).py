T = int(input())

for test_case in range(1,T+1):
    k, n, m = map(int,input().split())
    charge_station = set(list(map(int,input().split())))

    position = 0 # 현 위치 
    charge_cnt = 0 # 충전 횟수

    while position + k < n :    # 현재 위치와 이동 가능 거리 포함이 n 보다 작을 때 돌림
        next_p = position + k   # 다음 지정 위치
        while next_p > position and next_p not in charge_station:   # 다음 지정 위치가 현 위치 보다 크고, 충전리스트에 없을 때
            next_p -= 1     # 뒤로 1칸씩 빼면서 충전기 찾아감
        
        if next_p == position:  # 만약 다음 지정 위치에서부터 뒤로 오면서 충전기가 안 보이면 목적지 도달 못함. 즉시 종료
            charge_cnt = 0
            break

        position = next_p   # 충전기 찾고 , 충전 후 현재 위치를 갱신함.
        charge_cnt += 1     # 충전 카운트 1올리기

    print(f'#{test_case} {charge_cnt}')