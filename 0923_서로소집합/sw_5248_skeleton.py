import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/ssafy_algorithm/ssafy_algorithm/0923_서로소집합/sw_5248.txt')

def find_set(x):
    if x != p_list[x]:  # 부모노드와 내가 다르다면, 즉, 대표자가 아님
        p_list[x] = find_set(p_list[x]) # 결국 대표자를 만나서, 대표자가 반환되면서 모든 부모의 값이 대표자로 갱신
    return p_list[x]

def union_set(x,y):
    # x의 대표와 y의 대표를 가져온다
    px = find_set(x)
    py = find_set(y)

    # 이미 같은 그룹이면 합칠 필요가 없음
    if px != py:    # 서로 다른 그룹일 경우에만 합친다.
        if rank[px] > rank[py]: # 랭크가 높은 쪽으로 낮은 애가 붙는다.
            p_list[py] = px
        elif rank[px] < rank[py]:
            p_list[px] = py
        else:
            p_list[py] = px
            rank[px] += 1

T = int(input())
for tc in range(1, T+1):
    # N = 전체 사람 번호
    # M = 제출된 쪽지의 수
    N, M = map(int, input().split())
    edge = list(map(int, input().split()))  # 간선 정보

    # make_set() -> 스스로를 집합으로 만드는 기능
    p_list = list(range(N+1))
    rank = [0] * (N+1) # Union에서 Rank 최적화용 리스트

    # 쪽지의 개수만큼 반복하면서, 쪽지에 적혀있는 친구 2명을 가져온다.
    # 그리고 친구 2명을 Union해서 그룹화해주고, 모든 쪽지에 해당하는 친구를 그룹화
    for i in range(M):
        x = edge[i*2]
        y = edge[i*2 + 1]
        union_set(x,y)
    

    # 최적화를 쫙 해주는 느낌
    # for i in range(1,N+1):
    #     p_list[i] = find_set(i)

    # 결국 우리가 원하는건 그룹의 수
    # 그룹의 수 -> 대표자의 수
    print(f'#{tc} {len(set(p_list)) - 1}')
