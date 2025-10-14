T = int(input())
for test_case in range(1, T + 1):
    topping_cnt, limit_k = map(int, input().split())
    toppings = [list(map(int, input().split())) for _ in range(topping_cnt)]
    result = 0


    def dfs(depth, total_score, total_calorie):
        global result
        # 가지치기할 수 있어요...
        # limit_k를 넘어서는 경우에는 재료를 더 선택하고 자시고 할 필요가 없다 ( 음수인 칼로리는 없으니까)
        if total_calorie > limit_k:
            return

        # 종료 조건
        # 모든 토핑을 다 고려한 경우(선택을 하든, 안하든)
        # 맛의 최대값을 갱신한다.
        if depth == topping_cnt:
            result = max(result, total_score)
            return

        # 재료를 선택한 경우
        dfs(depth + 1, total_score + toppings[depth][0], total_calorie + toppings[depth][1])

        # 재료를 선택하지 않은 경우
        dfs(depth + 1, total_score, total_calorie)

    """
    dfs
    파라미터
    1. 재귀호출을 종료하는 조건 => 토핑을 몇 개 선택했는가. => 주어진 토핑 개수에 도달하면 => 종료 
    2. 누적해서 가져가고 싶은 값 => 누적해서 선택한 토핑들의 누적 칼로리, 누적 점수 
    """
    dfs(0, 0, 0)

    print(f"#{test_case} {result}")
