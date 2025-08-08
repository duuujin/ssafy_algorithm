T = int(input())
for test_case in range(1, T+1):
    n,m = map(int,input().split())
    arr = [input().strip() for _ in range(n)]

    result = ""
    for i in range(n):
        for j in range(n - m + 1):
            word = arr[i][j:j+m]
            if word == word[::-1]:
                result = word
                break
            if result != "":
                break
    print(result)