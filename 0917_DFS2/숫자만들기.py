def dfs(depth, value, plus, minus, mul, div):
    global max_value, min_value, N, numbers
    if depth == N:
        max_value = max(max_value, value)
        min_value = min(min_value, value)
        return

    if plus > 0:
        dfs(depth + 1, value + numbers[depth], plus - 1, minus, mul, div)
    if minus > 0:
        dfs(depth + 1, value - numbers[depth], plus, minus - 1, mul, div)
    if mul > 0:
        dfs(depth + 1, value * numbers[depth], plus, minus, mul - 1, div)
    if div > 0:

        if value < 0:
            dfs(depth + 1, -(-value // numbers[depth]), plus, minus, mul, div - 1)
        else:
            dfs(depth + 1, value // numbers[depth], plus, minus, mul, div - 1)


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    plus, minus, mul, div = map(int, input().split())
    numbers = list(map(int, input().split()))
    max_value = -1e9
    min_value = 1e9
    dfs(1, numbers[0], plus, minus, mul, div)

    print(f"#{t} {max_value - min_value}")