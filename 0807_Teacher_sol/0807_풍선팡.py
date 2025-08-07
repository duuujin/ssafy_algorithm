dxy = [[0,1],[0,-1],[1,0],[-1,0]]

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int,input().split()))
    arr = [list(map(int,input().split())) for _ in range(N)] 

    # 꽃가루의 합 중에서 최대값이 가장 큰 값을 저장할 변수
    max_vlaue = 0

    # 모든 풍선을 순회하고, 터트린다.
    for i in range(N): # 행
        for j in range(M): # 열
            # i, j에서 풍선을 터트렸을 때, 발생하는 꽃가루를 저장할 누적 변수를 만들어야 함
            temp_sum = arr[i][j] # 본인 꽃가루도 포함하기 때문에 바로 포함해서 초기화
            
            # 기준점 잡았으니 델타 탐색 시작
            # dxy = [[0,1],[0,-1],[1,0],[-1,0]]
            # 처음 for 돌 때 [0,1] => [dx, dy]
            # dx : 0 dy : 1 => 오른쪽
            for dx,dy in dxy:
                # 각 방향으로 한 번 만 탐색 x -> 몇번탐색? -> 꽃가루 개수만큼(arr[i][j])
                for dist in range(1, arr[i][j] + 1): # arr[i][j] -> 1 일 경우에는 , 그대로 dist 1밖에 실행 안된다.
                    # 델타탐색으로 다음에 이동할 좌표
                    ni = i + dx*dist
                    nj = y + dy*dist

                    # 범위를 벗어날 것. 
                    # 꽃가루의 누적은 범위 안에 있는 애들한테만 해당.
                    if 0 <= ni < N and 0 <= j < M:
                        temp_sum += arr[ni][nj]
                    else: # 범위를 벗어난 경우
                        break
                
            temp_sum = max(max_vlaue, temp_sum)

    print(f'#{tc} {max_vlaue}')