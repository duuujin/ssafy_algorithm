import heapq

def prim(v, edges):
    graph = [[] for _ in range(v + 1)]
    for n1, n2, w in edges:
        graph[n1].append((w, n2))
        graph[n2].append((w, n1))

    visited = [False] * (v + 1)
    min_heap = [(0, 1)]  # (비용, 시작정점)
    total_weight = 0
    connected_nodes = 0

    while min_heap:
        w, node = heapq.heappop(min_heap)
        if visited[node]:
            continue
        visited[node] = True
        total_weight += w
        connected_nodes += 1

        for next_w, next_node in graph[node]:
            if not visited[next_node]:
                heapq.heappush(min_heap, (next_w, next_node))

    # 모든 노드가 연결되지 않았으면 -1 반환
    if connected_nodes < v:
        return -1
    return total_weight

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        n1, n2, w = map(int, input().split())
        edges.append((n1, n2, w))

    result = prim(N, edges)
    print(f"#{test_case} {result}")