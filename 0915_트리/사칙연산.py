def inord(n):
    if n <= N:
        left = inord(n * 2)        # 왼쪽 계산
        right = inord(n * 2 + 1)   # 오른쪽 계산

        # 현재 노드가 연산자인 경우
        if lst[n] in '+-*/':
            if lst[n] == '+':
                return left + right
            elif lst[n] == '-':
                return left - right
            elif lst[n] == '*':
                return left * right
            elif lst[n] == '/':
                return left / right
        else:  # 숫자이면 float로 반환
            return float(lst[n])
    return 0  # 존재하지 않는 노드

# -----------------------------
T = 10
for test_case in range(1, T+1):
    N = int(input())
    lst = [0] * (N + 1)
    for i in range(1, N + 1):
        tlist = input().split()
        lst[i] = tlist[1]  # 값만 저장 (숫자 혹은 연산자)

    # 루트 노드에서 계산 시작
    result = int(inord(1))  # 소수점 버림
    print(f'#{test_case} {result}')
