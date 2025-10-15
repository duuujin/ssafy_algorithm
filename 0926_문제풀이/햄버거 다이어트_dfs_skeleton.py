def dfs(depth, total_score, total_calorie):
    global result
    if total_calorie > limit_c:
        return

    if depth == toping_cnt:
        result = max(result, total_score)
        return

    dfs(depth + 1, total_score + topings[depth][0], total_calorie + topings[depth][1])

    dfs(depth + 1, total_score,total_calorie)

T = int(input().strip())
for test_case in range(1,T+1):
    toping_cnt, limit_c = map(int,input().split())
    topings = [list(map(int,input().split())) for _ in range(toping_cnt)]
    result = 0

    dfs(0, 0, 0)
    print(f'#{test_case} {result}')