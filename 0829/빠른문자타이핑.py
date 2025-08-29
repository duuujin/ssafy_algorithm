T = int(input())
for test_case in range(1,T+1):
    cnt = 0
    a,b = map(str,input().split())     
    mun = a.split(b)

    result = list("".join(mun))
    for i in range(len(result)):
        cnt += 1

    mun.pop()
    answer = len(mun)+len(result)
    
    print(f'#{test_case} {answer}')
    