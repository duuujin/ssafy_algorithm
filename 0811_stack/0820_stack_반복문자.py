T = int(input())
for test_case in range(1,T+1):
    s = input()
    stack = []

    for i in s:
        if not stack: # 스택이 없으면, 입력받아온 문자열에서 하나씩 추가.
            stack.append(i)
        else:
            if i == stack[-1]: # 스택의 최상단부터 i랑 같은지 확인 같다면, 제거
                stack.pop()
            else:
                stack.append(i) # 다르다면, stack 리스트에 추가
    print(f'#{test_case} {len(stack)}')