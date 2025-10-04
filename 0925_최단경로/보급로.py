import heapq
from collections import deque
def bfs(arr, x, y)
    

T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    map = [list(map(int,input().split())) for _ in range(n)]

    result = bfs(map,0,0)