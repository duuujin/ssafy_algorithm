from collections import deque

def bfs():
    graph = [[] for _ in range(101)]
    for i in range(0, leng, 2):
        f, t = arr[i], arr[i + 1]
        graph[f].append(t)

    visited = [False] * 101
    queue = deque([st])
    visited[st] = True

    last = []
    while queue:
        size = len(queue)
        last = []
        for _ in range(size):
            node = queue.popleft()
            last.append(node)
            for neigh in graph[node]:
                if not visited[neigh]:
                    visited[neigh] = True
                    queue.append(neigh)

    return max(last)


T = 10
for test_case in range(1, T + 1):
    leng, st = map(int, input().split())
    arr = list(map(int, input().split()))
    result = bfs()
    print(f"#{test_case} {result}")
