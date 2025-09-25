import heapq , math
def dijkstra(n,edges, start):
    graph = [[] for _ in range(n+1)]
    for u, v, w in edges:
        graph[u].append((v,w))

    distances = [math.inf] * (n+1)
    distances[start] = 0
    min_heap = []
    heapq.heappush(min_heap, (0, start))

    while min_heap:
        current_distance , current_vertex  = heapq.heappop(min_heap)

        if distances[current_vertex] < current_distance : continue

        for adjacent, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(min_heap, (distance, adjacent))
    return distances
    
        
T = int(input())
for test_case in range(1,T+1):
    n,m = map(int,input().split())
    edges = [list(map(int,input().split())) for _ in range(m)]

    start_v = 0
    res = dijkstra(n, edges, start_v)
    print(f'#{test_case} {res[n]}')


# -------------------딕셔너리 형태--------------------------------------------
import heapq, math

def dijkstra(n, edges, start):
    # 1. 그래프 생성
    graph = {i: {} for i in range(n+1)}
    for u, v, w in edges:
        graph[u][v] = w 

    # 2. 거리 초기화
    distances = {v: math.inf for v in graph}
    distances[start] = 0

    min_heap = [(0, start)]

    while min_heap:
        current_distance, current_vertex = heapq.heappop(min_heap)

        if distances[current_vertex] < current_distance:
            continue

        for adjacent, weight in graph[current_vertex].items():
            new_distance = current_distance + weight
            if new_distance < distances[adjacent]:
                distances[adjacent] = new_distance
                heapq.heappush(min_heap, (new_distance, adjacent))

    return distances


T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]

    start_v = 0
    res = dijkstra(n, edges, start_v)

    print(f'#{test_case} {res[n]}')
