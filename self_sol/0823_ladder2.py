import sys
sys.stdin = open("/Users/chaeng/Desktop/duujin/ssafy_algorithm/self_sol/input (5).txt","r")
for test_case in range(1,11):
    T = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    visited = [[False] * 100 for _ in range(100)]
    