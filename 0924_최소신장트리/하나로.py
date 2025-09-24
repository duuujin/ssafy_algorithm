import heapq

T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    x_list = list(map(int,input().split()))
    y_list = list(map(int,input().split()))
    e = float(input())
    
    vertices = [(x, y) for x, y in zip(x_list, y_list)]

    visited = [False] * n
    min_heap = [(0,0)]
    total_cost = 0
    cnt = 0

    while min_heap and cnt < n:
        cost,u = heapq.heappop(min_heap)
        if visited[u]: continue
        visited[u] = True
        total_cost += cost
        cnt += 1
        for v in range(n):
            if not visited[v]:
                dist = (vertices[u][0] - vertices[v][0])**2 + (vertices[u][1] - vertices[v][1])**2
                heapq.heappush(min_heap, (dist * e, v))
    print(f'#{test_case} {round(total_cost)}')