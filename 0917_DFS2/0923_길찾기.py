from collections import defaultdict,deque

def bfs(st):
    queue = deque()
    queue.append(st)
    visited = [False] * 100
    visited[st] = True

    while queue:
        x = queue.popleft()
        if x == 99:
            return True
        for next in graph[x]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
    return False
    

for test_case in range(1,11):
    T , N = map(int,input().split())
    arr = list(map(int,input().split()))
    
    graph = defaultdict(list)

    for i in range(N):
        graph[arr[2*i]].append(arr[2*i+1])
    
    found = bfs(0)

    
    if found == True:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')