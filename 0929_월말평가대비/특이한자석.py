from collections import deque

T = int(input())
for test_case in range(1,T+1):
    K = int(input())
    N = 4
    magnet_list = [deque(list(map(int,input().split()))) for _ in range(N)]
    for _ in range(K):
        num, di = map(int,input().split())
        num -= 1 

        dirs = [0] * 4
        dirs[num] = di

        