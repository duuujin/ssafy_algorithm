T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    arr = list(map(int,input().split()))
    max_cnt = 0

    for i in range(n):
        nak = 0
        for j in range(i+1,n):
            if arr[i] <= arr[j] :
                nak += 0 
            elif arr[i] > arr[j]:
                nak += 1
        max_cnt = max(max_cnt, nak)
    
    print(f'#{test_case} {max_cnt}')