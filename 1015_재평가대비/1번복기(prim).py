import heapq
def prim(N, M):
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        n1, n2, w = map(int,input().split())
        graph[n1].append((w, n2))
        graph[n2].append((w, n1))
    visited = [False] * (N + 1)
    min_heap = [(0,1)]
    total_weight = 0
    edge_count = 0

    while min_heap:
        w, node = heapq.heappop(min_heap)
        if visited[node]:
            continue

        visited[node] = True
        total_weight += w
        edge_count += 1

        for next_w, next_node in graph[node]:
            if not visited[next_node]:
                heapq.heappush(min_heap, (next_w, next_node))

    if edge_count != N:
        return -1
    return total_weight

T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    result = prim(N, M)
    print(f'#{test_case} {result}')