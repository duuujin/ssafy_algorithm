T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    paint1 = list(map(int,input().split())) # paint리스트는 왼쪽 위 좌표 2개 , 오른쪽 아래 좌표 2개 , 컬러 코드(1은 빨강, 2는 파랑)이다.
    paint2 = list(map(int,input().split()))
    dxy = [[0,1],[0,-1],[1,0],[-1,0]]

    

    