from collections import defaultdict

# 후위순회로 구현
def dfs(v):
    visited[v] = True
    
    # 인접한 정점들을 다시 호출 
    for nei in graph[v]:
        # 인접 정점들 중 방문한 적 없을 때만 DFS실행
        if not visited[nei]:
            dfs(nei)
    
    # 더 이상 파고 들 때가 없을 경우에, 결과에 추가함.
    result.append(v)

T = 10
for test_case in range(1,T+1):
    v_cnt , e_cnt = map(int,input().split())
    edges = list(map(int,input().split()))

    # DAG 그래프 구성
    # 인접리스트 형태로 구성
    graph = defaultdict(list)

    # 시작점과 끝정점을 서로 연결해줌.
    for i in range(e_cnt):
        graph[edges[2*i]].append(edges[2*i+1])

    # 방문여부를 체크해야함.
    visited = [False] * (v_cnt+1)
    result = []

    """
    모든 정점에 대해서 DFS를 실행한다.
    - 연결되지 않은 그래프가 주어졌을 경우에도 모두 방문할 수 있도록
    (각 연결된 부분끼리의 순서만 올바르게 유지되면 아무 문제가 없다.)
    -> 그렇기 때문에 결과가 유일성 보장이 안됨.
    """
    for v in range(1,v_cnt+1):
        if not visited[v]: # 방문하지 않은 정점에서 DFS돌림
            dfs(v)

    print(f'#{test_case}',*result[::-1])
