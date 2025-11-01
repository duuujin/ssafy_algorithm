T = int(input())
for test_case in range(1, T + 1):
    topping_cnt, limit_k = map(int, input().split())
    toppings = [list(map(int, input().split())) for _ in range(topping_cnt)]
    result = 0

    def dfs(depth, total_score, total_calorie):
        global result
        if total_calorie > limit_k:
            return

        if depth == topping_cnt:
            result = max(result, total_score)
            return

        dfs(depth + 1, total_score + toppings[depth][0], total_calorie + toppings[depth][1])

        dfs(depth + 1, total_score, total_calorie)

    dfs(0, 0, 0)

    print(f"#{test_case} {result}")
