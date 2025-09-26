def dfs():
    pass


T = int(input())
for test_case in range(1, T + 1):
    # 토핑 수와 제한 칼로리
    topping_cnt, limit_k = map(int, input().split())
    # [[점수, 칼로리], ... ]
    toppings = [list(map(int, input().split())) for _ in range(topping_cnt)]
    result = 0

    dfs()

    print(f"#{test_case} {result}")
