import itertools
T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    half = n//2

    num_list = [i for i in range(n)]

    food_comb_list = itertools.combinations(num_list,half)

    res = float('INF')
    for a_food_list in food_comb_list:
        b_food_list = []

        for num in num_list:
            if num not in a_food_list:
                b_food_list.append(num)

        a_synergy_list = itertools.combinations(a_food_list,2)
        a_synergy_sum = 0
        for a_synergy in a_synergy_list:
            i,j = a_synergy
            a_synergy_sum += arr[i][j] + arr[j][i]

        b_synergy_lsit = itertools.combinations(b_food_list,2)
        b_synergy_sum = 0
        for b_synergy in b_synergy_lsit:
            i,j = b_synergy
            b_synergy_sum += arr[i][j] + arr[j][i]
        
        res = min(res, abs(a_synergy_sum - b_synergy_sum))
    print(f'#{test_case} {res}')

