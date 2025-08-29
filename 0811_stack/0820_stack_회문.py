T = 10
for test_case in range(1,11):
    n = int(input())
    arr = [list(map(str,input().split())) for _ in range(8)]
    palind_count = 0

    garo = 0