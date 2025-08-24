import sys
sys.stdin = open("/Users/chaeng/Desktop/duujin/ssafy_algorithm/self_sol/input (5).txt","r")
for test_case in range(1,11):
    T = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]  # 받아올 100*100 사다리 리스트
    visited = [[False] * 100 for _ in range(100)]   # 이동 한 위치 체크 배열
    cnt = 0 # 최단거리 카운트
    