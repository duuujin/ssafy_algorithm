from collections import deque

def bfs(start,goal, child, V):
    visited = [False] * (V+1)
    distance = [0] * (V+1)
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        node = queue.popleft()
        if node == goal:
            return distance[node]
        for next in child[node]:
            if not visited[next]:
                visited[next] = True
                distance[next] = distance[node] + 1
                queue.append(next)
    return 0

T = int(input())
for test_case in range(1,T+1):
    V , E = map(int,input().split())
    child = [[] for _ in range(V+1)]
    
    for _ in range(E):
        a, b = map(int,input().split())
        child[a].append(b)
        child[b].append(a)
    
    S, G = map(int,input().split())
    
    result = bfs(S, G, child, V)
    print(f'#{test_case} {result}')