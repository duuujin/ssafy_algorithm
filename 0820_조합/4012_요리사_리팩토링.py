import itertools

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]
    half = N // 2


    def get_synergy_sum(food_list, synergy):
        """
        주어진 식재료 리스트에 대한 시너지 합을 계산합니다.

        :param food_list: 식재료 리스트
        :param synergy: 시너지 값을 담은 2차원 리스트
        :return: 총 시너지 합
        """
        synergy_pairs = itertools.combinations(food_list, 2)
        synergy_sum = 0
        for i, j in synergy_pairs:
            synergy_sum += synergy[i][j] + synergy[j][i]
        return synergy_sum

    # 식재료를 인덱스로 표현
    # 식재료의 개수만큼 순차적인 인덱스 목록을 만든다.
    num_list = [i for i in range(N)]

    # A 요리와 B 요리는 식재료를 절반씩 나눠가져야 한다.
    # 식재료를 절반씩 나눠 가질 수 있는 모든 경우의 수를 구한다.
    # 그리고 절반씩 나눠가진 모든 경우의 수에서 맛의 차이가 적은 케이스를 구한다.
    food_comb_list = itertools.combinations(num_list, half)

    res = float('INF')  # 맛의 차이를 저장할 변수
    for a_food_list in food_comb_list:
        # a 식재료를 제외한 나머지 식재료를 b 식재료로 선정
        b_food_list = [num for num in num_list if num not in a_food_list]

        # 식재료 중에서 2개를 선택해서 만들 수 있는 모든 경우의 수를 구하기
        # 함수화 진행
        a_synergy_sum = get_synergy_sum(a_food_list, synergy)
        b_synergy_sum = get_synergy_sum(b_food_list, synergy)

        res = min(res, abs(a_synergy_sum - b_synergy_sum))
    print(f"#{test_case} {res}")


