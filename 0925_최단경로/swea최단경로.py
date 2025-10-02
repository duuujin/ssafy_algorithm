from collections import deque

T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n)]
