n = 5
martrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 모든 요소 순회

for i in range(n):
    for j in range(n):
        num_sum = 0
        # 델타 탐색 
        for k in range(4):
            ni = i + dx[k] # 다음 이동할 i 좌표
            nj = j + dy[k] # 다음 이동할 j 좌표
            
            # ni,nj는 범위를 벗어나면 안됨.
            if 0 <= ni < n and 0 <= nj < n:
                # 현재 좌표의 값과 이동한 좌표의 값의 차이 절대값
                num_sum += abs(martrix[i][j] - martrix[ni][nj])
        print("여기에 오면 델타 탐색을 끝내고 다 더한 값이 저장")