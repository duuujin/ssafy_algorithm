T = 10
for test_case in range(1,T+1):
    n = int(input())
    arr = list(map(int,input().split()))
    max_box = 0
    box_cnt = 0
    for i in range(100):
        c = max(arr,c)
        c -= 1
        box_cnt += 1
        b = min(arr,b)
        b += 1
        