T = int(input().strip())
for test_case in range(1, T+1):
    # N : 배열의 칸 수, M: 파리채의 크기
    N, M = list(map(int,input().split()))
    grid = [list(map(int,input().split())) for _ in range(N)] 

    # 우리가 원하는 건, 파리채로 죽일 수 있는 최대 파리의 수
    kill_flies_cnt = 0

    # 기준점을 잡기 위해서 grid를 순회한다.
    # 기준점을 기준으로 파리채를 찍어보고, 죽은 파리수를 센다.
    # 해당 기준점에 죽은 파리수가 현재까지의 죽인 파리수보다 크면 최대값 갱신
    # 파리채만큼의 범위를 확보하기 위해서 n-m+1 까지만 순회를 한다.
    for i in range(N-M+1): # 행 
        for j in range(N-M+1): # 열
            # (i,j)가 정해질때마다, 매번 초기화해서 다시 죽인 파리수를 게산 해야한다.
            tmp_sum = 0
            for m in range(M): # 행 
                for n in range(M): # 열
                    tmp_sum += grid[i+m][j+n]

            # tmp_sum에는 (i,j)에서 파리채로 죽인 누적 파리 수가 저장되어 있다.
            # if tmp_sum > kill_flies_cnt:
            #     kill_flies_cnt = tmp_sum

            kill_flies_cnt = max(kill_flies_cnt,tmp_sum) 
    print(f'#{test_case} {kill_flies_cnt}')