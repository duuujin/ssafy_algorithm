T = int(input().strip())
for test_case in range(1,T+1):
    n = int(input())
    num_list = list(map(int,input().split()))

    heap = [0]
    
    for x in num_list:
        heap.append(x)
        i = len(heap) - 1
        while i > 1 and heap[i] < heap[i // 2]:
            heap[i], heap[i // 2] = heap[i // 2], heap[i]
            i //= 2

    idx = len(heap) - 1
    total_sum = 0
    while idx > 1:
        idx //= 2
        total_sum += heap[idx]
    
    print(f'#{test_case} {total_sum}')