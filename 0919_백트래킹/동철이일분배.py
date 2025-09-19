import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/ssafy_algorithm/ssafy_algorithm/0919_백트래킹/1865_input.txt', "r")

# idx : 현재 선택 중인 직원을 의미
# per : 여태까지 선택한 직원들의 성공 확률을 누적한 값
def search(idx, per):
    global result

    # 이미 확률이 결과보다 적어졌다면, 굳이 뒤에 나오는 조합을 고려할 필요가 없다.
    if per <= result:
        return

    # 모든 직원이 전부 일을 분배한 경우, 최대값 갱신
    if idx == N:
        result = max(result,per)
        return
    # 직원이 몇 번 일을 맡을지 순회하는 로직
    # idx : 직원의 인덱스, i = 일(work)의 인덱스
    for i in range(N):
        if visited[i]: continue # 이미 누군가 일을 맡았다면, 이 일은 선택 할 수 없음.
        # idx에 해당하는 직원이 i번째 일을 맡으면, 맡았다고 visited를 업데이트 하고,
        # 다음 직원이 일을 또 고른다.
        visited[i] = True
        search(idx+1,per * arr[idx][i])
        # 이 일을 선택했던 경우를 원상복구 시켜야한다.
        visited[i] = False

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 제일 효율이 좋은 것을 찾는게 목표
    # 근데 입력값은 %로 주어짐
    # 71% * 63% -> 0.71 * 0.63 -> 연속으로 성공할 확률 (0.4473)
    # 입력받은 모든 수를 소수점으로 변환
    for i in range(N):
        for j in range(N):
            arr[i][j] /= 100
    # 순열
    # 해당 일이 담당자가 있는지를 확인하기 위한 변수를 만든다.
    # 인덱스에 해당하는 값이 1이라는건, 해당 일(index)는 누군가가 담당했으니, 제외하고 고려해라
    visited = [0]  * N
    result = 0 # 나올 수 있는 최대 성공률

    # DFS
    # 1. 종료시점을 결정할 파라미터 -> 각 직원을 선택하는 인덱스 -> 마지막 직원까지 모두 선택하면 그 때 확률을 갱신
    # 2. 누적해서 가져가고 싶은 값 -> 선택한 직원들의 최종 성공률
    search(0, 1)

    print(f'#{tc} {result}')