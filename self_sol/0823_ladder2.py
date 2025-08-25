import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\ssafy_algorithm\\ssafy_algorithm\\self_sol\\input (5).txt","r")
for test_case in range(1,11):
    T = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]  # 받아올 100*100 사다리 리스트
    # visited = [[False] * 100 for _ in range(100)]   # 이동 한 위치 체크 배열
    dxy = [[0,1],[0,-1],[1,0]]
    min_cnt = 100


    for i in range(100):
        if arr[0][i] == 1:
            x, y = (0, i)
            cnt = 0
            visited = [[False] * 100 for _ in range(100)]   # 이동 한 위치 체크 배열
            visited[x][y] = True

            while y < 100 :
                print("-----------------",x,y)
                for dx, dy in dxy:
                    nx = x+dx
                    ny = y+dy

                    if 0 <= nx < 100 and 0 <= ny < 100 and not visited[nx][ny] and visited[nx][ny] == 1:
                        visited[nx][ny] = True
                        print("@@@@@@@@@@@@@@@",x,y)
                        x, y = nx, ny
                        cnt += 1
            min_cnt = min(min_cnt,cnt)
    print(min_cnt)

