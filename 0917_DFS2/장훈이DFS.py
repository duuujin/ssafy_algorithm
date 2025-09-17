T = int(input())
for test_case in range(1,T+1):
    # n = 사람 수  , b = 목표 높이
    n , b = map(int,input().split())
    # 점원들의 키
    arr = list(map(int,input().split()))
    
    min_height = float('INF')

    # 밑 코드는 기본 베이스 코드, 모르면 외워두고 응용하기
    
    # idx : 현재 탐색 중인 직원의 인덱스
    # h_sum : 내가 선택해온 직원들의 키의 합
    def dfs(idx,h_sum):
        global min_height

        # 여태까지 선택한 직원들의 키의 합이 이미 우리가 선정한 최소값보다 커졌으면, 진행할 필요 없음
        # 가지치기 -> 백트래킹 기법
        if h_sum >= min_height:
            return

        # idx 가  n이 되면 , 모든 직원들에 대해서 선택 끝
        if idx == n:
            if h_sum >= b:
                min_height = min(min_height, h_sum)
            return
        
        # idx에 해당하는 직원을 선택한 경우
        dfs(idx+1,h_sum + arr[idx])

        # idx에 해당하는 직원을 선택하지 않은 경우
        dfs(idx+1, h_sum)
    
    """
    재귀함수의 파라미터
    DFS -> 스택 -> 재귀
    1. 재귀함수를 종료하기 위한 변수
    - 점원들을 모두 선택(포함하든/안하든) 했을 때
    - 현재 선택한 점원의 인덱스
    2. 누적해서 가져가고 싶은 값
    - 우리가 포함한 점원들 키의 합
    """

    dfs(0,0)

    print(f'#{test_case} {min_height-b}')