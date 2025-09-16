T = int(input())
for test_case in range(1,T+1):
    N,M = map(int,input().split())
    home = [list(map(int,input().split())) for _ in range(N)]
    K = 4
    cost = K*K+(K-1)*(K-1)
    