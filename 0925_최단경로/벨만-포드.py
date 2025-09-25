def bellman_ford(graph, start):
    v_count = len(graph)  # 그래프의 정점 수
    distances = {v: float('inf') for v in graph}
    distances[start] = 0

    # 모든 정점에 대해서 최단거리를 갱신하는데
    # 위 과정을 V-1 번 반복한다
    # 최단거리를 구하는데 최악의 경우에는 N개의 노드가 있을 때, N-1번의 간선을 통해서 최단거리가 갱신될 수 있다.
    for i in range(v_count - 1):
        updated = False # 거리가 없데이트된 적이 있는지를 확인하는 변수

        # 각 정점에 대해서 인접한 노드들 거리 갱신
        for u in graph:
            for v, weight in graph[u].items():
                # 시작 정점이 무한대라는건, 해당 정점까지 도달할 방법이 없다는 소리
                # 즉 , 갱신할 수 없다.
                # 무한대가 아니라면, 해당 정점까지의 최단 거리 + 다음 정점까지의 거리
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    updated = True
        
        # 거리가 갱신된 적이 없으면, 반복해서 거리를 갱신하는 패스를 끝낸다.
        if not updated:
            break

    for u in graph:
        for v, weight in graph[u].items():
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                print("음수 사이클이 발생했어요!")
                return

    return distances

# 예시 그래프
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': 3, 'D': 2, 'E': 3},
    'C': {'B': 1, 'D': 4, 'E': 5},
    'D': {'E': -3},
    'E': {'F': 2},
    'F': {}
}

# 시작 정점 설정
start_vertex = 'A'

# 벨만-포드 알고리즘 실행
result = bellman_ford(graph, start_vertex)

print(f"'{start_vertex}': {result}")
# 'A': {'A': 0, 'B': 3, 'C': 2, 'D': 5, 'E': 2, 'F': 4}