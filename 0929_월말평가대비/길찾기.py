from collections import deque
def bfs(n):
    queue = deque()
    queue.append(0)
    visited[0] = True
    while queue:
        node = queue.popleft()
        if node == 99 :
            return 1
        for next in graph[node]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
    return 0


for _ in range(1,11):
    T , N = map(int,input().split())
    edges = list(map(int,input().split()))
    
    graph = [[] for _ in range(100)]
    visited = [False] * 100

    for i in range(0, len(edges) , 2):
        a, b = edges[i] , edges[i+1]
        graph[a].append(b)

    result = bfs(0)
    print(f'#{T} {result}')