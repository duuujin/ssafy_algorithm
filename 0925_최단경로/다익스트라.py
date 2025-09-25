import heapq, math

def dijkstra(graph, start):
    # 모든 정점의 도달 최소 거리를 무한대로 초기화
    distances = {v: math.inf for v in graph}
    # 시작정점의 거리를 0으로 초기화
    distances[start] = 0
    # 거리가 갱신되는 정점을 저장할 우선순위 큐를 만든다.
    min_heap = []
    # [거리,정점]
    heapq.heappush(min_heap, [0, start])

    # 우선순위 큐가 빌 때까지 반복한다.
    while min_heap:
        # (우선순위 큐에서 노드 꺼내기) 해당 노드까지 도달하는 데 걸리는 거리, 노드
        current_distance, current_vertex = heapq.heappop(min_heap)

        # 해당 정점까지 도달하는 최소 거리보다 "이미 기존 노드까지의 거리"가 더 크면 그냥 skip
        # 이미 커버리면 어떤 노드로 가든 최단 거리갱신이 불가능하기 때문에 skip 한다.
        if distances[current_vertex] < current_distance: continue

        # 인접한 노드들을 순회
        for adjacent, weight in graph[current_vertex].items():
            # 현재까지 도달하는데 걸리는 최소 거리 + 다음 노드로 이동하는데 걸리는 거리
            distance = current_distance + weight
            # 해당 정점까지의 거리보다 짧게 거리가 나온다면 갱신한다.
            if distance < distances[adjacent]:
                # 갱신
                distances[adjacent] = distance
                # heapq에다가 다시 집어 넣어준다.
                heapq.heappush(min_heap, [distance, adjacent])
    
    return distances

graph = {
    'a' : {'b': 3, 'c' : 5},
    'b' : {'c': 2},
    'c' : {'b': 1, 'd' : 4, 'e' : 6},
    'd' : {'e': 2, 'f' : 3},
    'e' : {'f': 6},
    'f' : {}
}
start_v = 'a'
res = dijkstra(graph, start_v)
# {'a': 0, 'b': 3, 'c': 5, 'd': 9, 'e': 11, 'f': 12}