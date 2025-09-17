from itertools import combinations

T = int(input())
for test_case in range(1,T+1):
    # n = 사람 수  , b = 목표 높이
    n , b = map(int,input().split())
    # 점원들의 키
    arr = list(map(int,input().split()))

    # 점원들의 키의 합이 B를 넘되, 가장 작은 값
    min_height = float('INF')

    # 입력받은 arr에서 1명을 고르는 선택 , 2명, 3명 .. n명을 고르는 선택으로 모든 조합을 구함
    for r in range(1,n+1):
        comb_list = combinations(arr,r)
        for comb in comb_list:
            total_height = sum(comb)

            if total_height >= b:
                total_height = min(total_height, min_height)
    
    print(f'#{test_case} {total_height - b}')