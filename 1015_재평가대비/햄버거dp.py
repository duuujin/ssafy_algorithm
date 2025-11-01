T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    items = [list(map(int, input().split())) for _ in range(n)]

    dp = [0] * (m+1)
    for taste, cal in items:
        for c in range(m, cal-1, -1):
            if dp[c-cal] + taste > dp[c]:
                dp[c] = dp[c-cal] + taste
    print(f'#{tc} {max(dp)}')