def floyd_warshall(graph):
    V = len(graph)

    # 모든 정점을 경유 정점으로 고려한다
    for k in range(V):
        for i in range(V):  # 시작 정점을 고정하고
            # if i != k : continue
            for j in range(V): # 도착 정점을 고려한다
                # k를 경유해서 가냐 (graph[i][k] + graph[k][j])
                # 직항으로 i에서 j로 가냐(graph[i][j])
                # 직항으로 가는 경우가 더 먼 경우에는 경유하는 거리로 갱신한다
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    # 작은 값으로 갱신한다.
                    graph[i][j] = graph[i][k] + graph[k][j]
                    
    for i in range(V):
        if graph[i][i] < 0:
            print("음수 사이클이 존재합니다.")
            break
    
    return graph  

INF = float('inf')  # 무한대

# 예시 그래프의 인접 행렬
adj_matrix = [
    [0, 4, 2, 5, INF],
    [INF, 0, 1, INF, 4],
    [1, 3, 0, 1, 2],
    [-2, INF, INF, 0, 2],
    [INF, -3, 3, 1, 0]
]

result = floyd_warshall(adj_matrix)

# 최단 거리 행렬 출력 
for row in result:
    print(row)
# [0, 1, 2, 3, 4]
# [0, 0, 1, 2, 3]
# [-1, -1, 0, 1, 2]
# [-2, -1, 0, 0, 2]
# [-3, -3, -2, -1, 0]