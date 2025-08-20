T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    pa1,pa2,pa3,pa4,c= map(int,input().split()) # paint리스트는 왼쪽 위 좌표 2개 , 오른쪽 아래 좌표 2개 , 컬러 코드(1은 빨강, 2는 파랑)이다.
    fa1,fa2,fa3,fa4,c2 = map(int,input().split())
    arr = [[0]*10 for _ in range(10)]
    dxy = [[0,1],[0,-1],[1,0],[-1,0]]

    for i in range(pa1,pa3+1):
        for j in range(pa2,pa4+1):
            arr[i][j] += c
    
    for ii in range(fa1,fa3+1):
        for jj in range(fa3,fa4+1):
            arr[ii][jj] += c2
            
    print(arr)