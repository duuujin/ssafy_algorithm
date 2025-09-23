from collections import defaultdict
for test_case in range(1,11):
    T , N = map(int,input().split())
    arr = list(map(int,input().split()))

    graph = defaultdict(list)

    for i in range(N):
        graph[arr[2*i]].append(arr[2*i+1])
    
    visited = [False] * 100