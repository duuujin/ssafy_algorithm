T = int(input())
for test_case in range(1,T+1):
    k,n,m = map(int,input().split())
    charge_station = set(map(int,input().split()))

    position = 0
    charge_cnt = 0

    while position + k < n:
        next_position = position + k

        while next_position > position and next_position not in charge_station:
            next_position -= 1

            if next_position == position :
                charge_cnt = 0
                break
            
        position = next_position
        charge_cnt += 1

    print(f'#{test_case} {charge_cnt}')