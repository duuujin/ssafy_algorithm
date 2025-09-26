import heapq,math

def dijkstra(n, edges, start):
    graph = [[] for _ in range(n+1)]
    for u, v, w in edges:
        graph[u].append((v,w))

    distances = [math.inf] * (n+1)
    distances[start] = 0
    min_heap = []
    heapq.heappush(min_heap, (0,start))

    while min_heap:
        current_distance, current_veterx = heapq.heappop(min_heap)
        if distances[current_veterx] < current_distance: continue

        for adjacent, weight in graph[current_veterx]:
            distance = current_distance + weight
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(min_heap, (distance, adjacent))
    return distances


T = int(input())
for test_case in range(1,T+1):
    n, m = map(int,input().split())
    edges = [list(map(int,input().split())) for _ in range(m)]
    
    start_v = 0
    res = dijkstra(n, edges, start_v)
    if res[n-1] == math.inf:
        print(f'#{test_case} impossible')
    else:
        print(f'#{test_case} {res[n-1]}')