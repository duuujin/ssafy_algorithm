def floyd_warshall(graph):
    V = len(graph)

    for k in range(V):
        for i in range(V):
            for j in range(V): 
                if graph[i][k] + graph[k][j] < graph[i][j]:
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