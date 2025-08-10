# 문제 설명
# N×N 크기의 빙고판이 주어진다. 각 칸에는 'O' 또는 'X'가 있다.
# 각 'O' 칸에 대해 상, 하, 좌, 우에 위치한 'X'의 개수를 모두 합산하여 출력하라.
# 예제 입력
# 3
# OXO
# XXX
# OOX
# 출력
# 9
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(input())
arr = [list(input().strip()) for _ in range(n)]

count = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'O':
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 'X':
                    count += 1
print(count)