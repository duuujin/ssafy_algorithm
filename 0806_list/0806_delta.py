n = 5
martrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

total_sum = 0
# 주대각선의 합을 구하자
# 왼쪽 위 -> 오른쪽 아래
# 0,0 / 1,1 / 2,2 -> 즉, i == j
main_sum = 0
for i in range(n):
    for j in range(n):
        if i == j :
            main_sum += martrix[i][j]

# 역대각선의 합을 구하자
sub_sum = 0
for i in range(n):
    for j in range(n):
        if i == n - 1 - j:
            sub_sum += martrix[i][j]

# 가운데는 중첩으로 2번 더해졌으니, 가운데 값을 한 번 빼자.
middle_value = martrix[n // 2][ n // 2]

# 그 친구들을 다 합친 결과를 출력하자
total_sum = main_sum + sub_sum - middle_value
print(total_sum)