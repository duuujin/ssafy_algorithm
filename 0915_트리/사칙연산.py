def inord(n):
    if n > N :
        return 0
    left = inord(n * 2)
    right = inord(n * 2 + 1)

    if lst[n] in '+-*/':
        if lst[n] == '+':
            return left + right
        elif lst[n] == '-':
            return left - right
        elif lst[n] == '*':
            return left * right
        elif lst[n] == '/':
            return left / right
    else:  
        return float(lst[n])
    return 0  

# -----------------------------
T = 10
for test_case in range(1, T+1):
    N = int(input())
    lst = [0] * (N + 1)
    for i in range(1, N + 1):
        tlist = input().split()
        lst[i] = tlist[1]  

    result = int(inord(1))
    print(f'#{test_case} {result}')
