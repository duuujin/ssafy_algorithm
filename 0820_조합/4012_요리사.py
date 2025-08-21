import itertools

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]
    half = N // 2

    # 식재료를 인덱스로 표현
    # 식재료의 개수만큼 순차적인 인덱스 목록을 만든다.
    num_list = [i for i in range(N)]

    # A 요리와 B 요리는 식재료를 절반씩 나눠가져야 한다.
    # 식재료를 절반씩 나눠 가질 수 있는 모든 경우의 수를 구한다.
    food_comb_list = itertools.combinations(num_list, half)

    res = float('INF')  # 맛의 차이를 저장할 변수
    for a_food_list in food_comb_list:  # 하나의 조합은 A 식재료다
        # b 식재료로 a 식재료를 제외한 나머지 식재료를 선정
        b_food_list = []
        """
        아래 코드도 comprehesion으로 압축하기 
        """
        for num in num_list:
            if num not in a_food_list:
                b_food_list.append(num)
        """
        아래 두 개의 로직은 하나의 함수로 만들 수 있음 -> 함수화 페이지 ㄱㄱ
        """
        # a 식재료 중에서 2개를 선택해서 만들 수 있는 모든 경우의 수를 구하기
        a_synergy_list = itertools.combinations(a_food_list, 2)
        a_synergy_sum = 0
        for a_synergy in a_synergy_list:
            i, j = a_synergy
            a_synergy_sum += synergy[i][j] + synergy[j][i]

        b_synergy_list = itertools.combinations(b_food_list, 2)
        b_synergy_sum = 0
        for b_synergy in b_synergy_list:
            i, j = b_synergy
            b_synergy_sum += synergy[i][j] + synergy[j][i]

        res = min(res, abs(a_synergy_sum - b_synergy_sum))
    print(f"#{test_case} {res}")
